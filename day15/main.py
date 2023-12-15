from utils import *
import re

def processInput(data):
  return data[0].split(',')

def runHash(s):
  c = 0
  for cr in s:
    c += ord(cr)
    c = (c * 17) % 256
  return c

def main(raw, part):
  total = 0

  data = processInput(raw)

  if part == 1:  
    for cmd in data:
      # print(cmd, runHash(cmd))
      total += runHash(cmd)
    return total
  elif part == 2:
    datas = [[] for i in range(256)]
    for cmd in data:
      label = re.match('[a-z]+', cmd)[0]
      box = runHash(label)
      op = cmd[len(label)]
      if op == '-':
        datas[box] = [c for c in datas[box] if c[0] != label]
      elif op == '=':
        num = cmd[len(label) + 1]
        assert num in '123456789'
        if any(c[0] == label for c in datas[box]):
          datas[box] = [(label,num) if c[0] == label else c for c in datas[box]]
        else:
          datas[box].append((label,num))
      
    total = 0

    for i__, box in enumerate(datas):
      i = i__+1
      for j__,c in enumerate(box):
        j = j__+1
        label,num = c
        total += i * j * int(num)
  
    return total
  return total

if __name__ == '__main__':
  part1_sample = main(readFileName('s.txt'), 1)
  print('Part 1 (sample):', part1_sample)
  assert part1_sample == 1320

  part1_real = main(readFileName('r.txt'), 1)
  print('Part 1 (real):', part1_real)
  assert part1_real == 497373

  part2_sample = main(readFileName('s.txt'), 2)
  print('Part 2 (sample):', part2_sample)
  assert part2_sample == 145

  part2_real = main(readFileName('r.txt'), 2)
  print('Part 2 (real):', part2_real)
  # assert part2_real == 0

