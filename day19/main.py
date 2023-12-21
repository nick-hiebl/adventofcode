from utils import *
import re
from math import prod

toInd = { 'x': 0, 'm': 1, 'a': 2, 's': 3 }

def processInput(data):
  flows = {}
  parts = []

  x = '\n'.join(data)
  fs,ps = x.split('\n\n')
  fs2 = fs.split('\n')
  ps2 = ps.split('\n')

  for line in fs2:
    name,content = line[:-1].split('{')
    rules = content.split(',')
    flows[name] = rules
  
  for p in ps2:
    parts.append(tuple(int(x) for x in re.findall('[0-9]+', p)))
    # print(parts[-1])

  return flows, parts

def checkAccepted(flows, part, wkf):
  rules = flows[wkf]
  for rule in rules:
    if rule == 'A':
      return True
    elif rule == 'R':
      return False
    elif ':' in rule:
      cond,nex = rule.split(':')
      c = toInd[cond[0]]
      comp = cond[1]
      v = int(cond[2:])
      if (comp == '<' and part[c] < v) or (comp == '>' and part[c] > v):
        if nex == 'A':
          return True
        elif nex == 'R':
          return False
        else:
          return checkAccepted(flows, part, nex)
    else:
      return checkAccepted(flows, part, rule)

def checkAcceptRanges(flows, ranges, wkf, index, depth = 0):
  print('   '*depth, 'Investigating', wkf, 'with', ranges)
  if wkf == 'A':
    res = prod(hi-lo + 1 for lo,hi in ranges)
    print('   '*depth, 'COMPUTING', ranges, res)
    return res
  elif wkf == 'R':
    return 0
  rules = flows[wkf]
  for i,rule in enumerate(rules):
    if i < index:
      continue

    if rule == 'A':
      res = prod(hi-lo + 1 for lo,hi in ranges)
      print('   '*depth, 'COMPUTING', ranges, res)
      return res
    elif rule == 'R':
      return 0
    elif ':' in rule:
      print('   '*depth, 'Examining rule:', rule)
      cond,nex = rule.split(':')
      c = toInd[cond[0]]
      comp = cond[1]
      v = int(cond[2:])
      lo,hi = ranges[c]
      if comp == '<':
        # (A,B) < V
        print('   '*depth, comp, v, (lo,hi))
        if v <= lo:
          continue
        elif v > hi:
          return checkAcceptRanges(flows, ranges, nex, 0, depth+1)
        else:
          includeRanges = tuple((l,h) if j != c else (l,v - 1) for j,(l,h) in enumerate(ranges))
          excludeRanges = tuple((l,h) if j != c else (v,h) for j,(l,h) in enumerate(ranges))
          return checkAcceptRanges(flows, includeRanges, nex, 0, depth+1) + checkAcceptRanges(flows, excludeRanges, wkf, index + 1, depth+1)
      else:
        # (A,B) > V
        print('   '*depth, comp, v, (lo,hi))
        if v < lo:
          return checkAcceptRanges(flows, ranges, nex, 0, depth+1)
        elif v >= hi:
          continue
        else:
          includeRanges = tuple((l,h) if j != c else (v+1,h) for j,(l,h) in enumerate(ranges))
          excludeRanges = tuple((l,h) if j != c else (l,v) for j,(l,h) in enumerate(ranges))
          return checkAcceptRanges(flows, includeRanges, nex, 0, depth+1) + checkAcceptRanges(flows, excludeRanges, wkf, index + 1, depth+1)
    else:
      return checkAcceptRanges(flows, ranges, rule, 0, depth+1)
    

def checkBounds(rules):
  points = ([], [], [], [])

  for flow in rules.values():
    for rule in flow:
      # print(rule)
      if '<' in rule or '>' in rule:
        cond,nex = rule.split(':')
        c = toInd[cond[0]]
        comp = cond[1]
        v = int(cond[2:])
        
        points[c].append(comp + str(v))
  
  for p in points:
    p.sort()
  print(points)
  print(list(len(p) for p in points))


def main(raw, part):
  total = 0

  flows, parts = processInput(raw)

  if part == 1:
    for p in parts:
      if checkAccepted(flows, p, 'in'):
        total += sum(p)
    return total
  elif part == 2:
    # checkBounds(flows)
    # for cmd in data:
    #   pass
    return checkAcceptRanges(flows, tuple((1,4000) for i in range(4)), 'in', 0)

if __name__ == '__main__':
  part1_sample = main(readFileName('s.txt'), 1)
  print('Part 1 (sample):', part1_sample)
  assert part1_sample == 19114

  part1_real = main(readFileName('r.txt'), 1)
  print('Part 1 (real):', part1_real)
  assert part1_real == 353553

  part2_sample = main(readFileName('s.txt'), 2)
  print('Part 2 (sample):', part2_sample)
  assert part2_sample == 167409079868000

  part2_real = main(readFileName('r.txt'), 2)
  print('Part 2 (real):', part2_real)
  # assert part2_real == 0
