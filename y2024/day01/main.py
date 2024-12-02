from utils import *
import re

def processInput(data):
  left, right = [], []

  for line in data:
    a,b = list(map(int, line.split()))
    left.append(a)
    right.append(b)

  return left, right

def main(raw, part):
  total = 0

  left, right = processInput(raw)

  if part == 1:
    total = sum(abs(a - b) for a,b in zip(sorted(left), sorted(right)))

    return total
  elif part == 2:
    rs = counts_of_iterable(right)
    for a in left:
      total += a * rs[a]
    return total

if __name__ == '__main__':
  part1_sample = main(readFileName('s.txt'), 1)
  print('Part 1 (sample):', part1_sample)
  assert part1_sample == 11

  part1_real = main(readFileName('r.txt'), 1)
  print('Part 1 (real):', part1_real)
  assert part1_real == 1197984

  part2_sample = main(readFileName('s.txt'), 2)
  print('Part 2 (sample):', part2_sample)
  assert part2_sample == 31

  part2_real = main(readFileName('r.txt'), 2)
  print('Part 2 (real):', part2_real)
  assert part2_real == 23387399
