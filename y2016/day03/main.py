from utils import *
import re

def processInput(data, part=1):
  out = []

  for line in data:
    out.append(tuple(map(int, re.split(r'\s+', line))))

  if part == 2:
    return sum((list(zip(*b)) for b in bundle(out, 3)), [])

  return out

def is_valid(tri):
  long = max(tri)
  others = sum(tri) - long
  return long < others

def main(raw, part):
  total = 0

  data = processInput(raw, part)

  return sum(int(is_valid(tri)) for tri in data)

if __name__ == '__main__':
  part1_sample = main(readFileName('s.txt'), 1)
  print('Part 1 (sample):', part1_sample)
  assert part1_sample == 3

  part1_real = main(readFileName('r.txt'), 1)
  print('Part 1 (real):', part1_real)
  assert part1_real == 1050

  part2_sample = main(readFileName('s.txt'), 2)
  print('Part 2 (sample):', part2_sample)
  assert part2_sample == 6

  part2_real = main(readFileName('r.txt'), 2)
  print('Part 2 (real):', part2_real)
  # assert part2_real == 0
