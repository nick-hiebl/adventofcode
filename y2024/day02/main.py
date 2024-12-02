from utils import *
import re

def processInput(data):
  out = []

  for line in data:
    out.append(list(map(int, line.split())))

  return out

def is_valid_ord(d):
  return tuple(d) == tuple(sorted(d)) or tuple(d) == tuple(sorted(d, reverse=True))

def is_valid(d):
  if not is_valid_ord(d):
    return False
  
  diffs = [abs(a-b) for a,b in zip(d, d[1:])]
  return all(0 < d <= 3 for d in diffs)

def main(raw, part):
  total = 0

  data = processInput(raw)

  if part == 1:
    for cmd in data:
      if is_valid(cmd):
        total += 1
    return total
  elif part == 2:
    for cmd in data:
      if is_valid(cmd):
        total += 1
      else:
        for i in range(len(cmd)):
          if is_valid(cmd[:i] + cmd[i+1:]):
            total += 1
            break
    return total

if __name__ == '__main__':
  part1_sample = main(readFileName('s.txt'), 1)
  print('Part 1 (sample):', part1_sample)
  assert part1_sample == 2

  part1_real = main(readFileName('r.txt'), 1)
  print('Part 1 (real):', part1_real)
  assert part1_real == 341

  part2_sample = main(readFileName('s.txt'), 2)
  print('Part 2 (sample):', part2_sample)
  assert part2_sample == 4

  part2_real = main(readFileName('r.txt'), 2)
  print('Part 2 (real):', part2_real)
  assert part2_real == 404
