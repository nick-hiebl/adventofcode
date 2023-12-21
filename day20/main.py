from utils import *
import re
from parse import *
from queue import deque

def processInput(data):
  out = { 'rx': ('', [], {}) }

  for line in data:
    ins, outs = line.split(' -> ')
    recps = outs.split(', ')
    name = ins
    pre_op = ''
    if name[0] in ('&', '%'):
      pre_op = name[0]
      name = name[1:]

    config = {}
    if pre_op == '%':
      config['state'] = 'low'
    
    out[name] = (pre_op, recps, config)
  
  for line in data:
    ins, outs = line.split(' -> ')
    recps = outs.split(', ')
    name = ins
    if name[0] in ('&', '%'):
      name = name[1:]
    for r in recps:
      kind, rs2, D2 = out[r]
      if kind == '&':
        D2[name] = 'low'

  return out

def processPulses(data):
  queue = deque()
  queue.append(('broadcaster', 'low', 'button'))

  lows = 0
  highs = 0

  while len(queue):
    node, level, parent = queue.popleft()

    if level == 'low':
      lows += 1
    elif level == 'high':
      highs += 1

    operator, children, info = data[node]

    # print('{} -{}-> {}'.format(parent, level, node))

    if operator == '':
      for child in children:
        queue.append((child, level, node))
    elif operator == '%':
      if level == 'high':
        continue
      elif level == 'low':
        output = 'low' if info['state'] == 'high' else 'high'
        info['state'] = output
        for child in children:
          queue.append((child, output, node))
    elif operator == '&':
      info[parent] = level
      output = 'low' if all(l == 'high' for l in info.values()) else 'high'
      for child in children:
        queue.append((child, output, node))

  return lows, highs

def processPulses2(data, checks):
  queue = deque()
  queue.append(('broadcaster', 'low', 'button'))

  while len(queue):
    node, level, parent = queue.popleft()

    if (node,level,parent) in checks:
      return (node,level,parent)

    operator, children, info = data[node]

    # print('{} -{}-> {}'.format(parent, level, node))

    if operator == '':
      for child in children:
        queue.append((child, level, node))
    elif operator == '%':
      if level == 'high':
        continue
      elif level == 'low':
        output = 'low' if info['state'] == 'high' else 'high'
        info['state'] = output
        for child in children:
          queue.append((child, output, node))
    elif operator == '&':
      info[parent] = level
      output = 'low' if all(l == 'high' for l in info.values()) else 'high'
      for child in children:
        queue.append((child, output, node))

  return False

def main(raw, part):
  total = 0

  data = processInput(raw)

  if part == 1:
    lows = 0
    highs = 0
    for i in range(1000):
      lo,hi = processPulses(data)
      lows += lo
      highs += hi
    return lows * highs
  elif part == 2:
    i = 0

    first = {}

    try:
      while True:
        i += 1
        # done = processPulses2(data, [('rx', 'low')])
        # rk - 3733
        # cd - 3793
        # zf - 3947
        done = processPulses2(data, [('gh', 'high', 'qx')])
        # done = processPulses2(data, [('rk', 'low')])
        # done = processPulses2(data, [('jj', 'high')])
        if done:
          print(i, done)
          break
        # if i % 1 == 0:
        #   cs = data['jj'][2]
        #   for name in cs:
        #     on = cs[name]
        #     if name in first or on == 'low':
        #       continue
        #     first[name] = i
        #     print(i, first, cs)
        #   o = list(1 if x == 'high' else 0 for x in cs.values())
        #   if len(list(first.keys())) == len(o):
        #     print(i, first)
        #     break
        #   # print(i, o, cs)
        # if i > 1000:
        #   break
      return i
    except:
      print('Aborted:', i)
      return i

if __name__ == '__main__':
  part1_sample = main(readFileName('s.txt'), 1)
  print('Part 1 (sample):', part1_sample)
  assert part1_sample == 32000000

  part1_real = main(readFileName('r.txt'), 1)
  print('Part 1 (real):', part1_real)
  assert part1_real == 730797576

  # part2_sample = main(readFileName('s.txt'), 2)
  # print('Part 2 (sample):', part2_sample)
  # assert part2_sample == 0

  part2_real = main(readFileName('r.txt'), 2)
  print('Part 2 (real):', part2_real)
  # assert part2_real == 0
