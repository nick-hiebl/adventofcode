from utils import *
import re

def processInput(data):
  out = []

  for line in data:
    out.append(line)

  return out

def is_real(code):
  base, check_sum = code[:-1].split('[')
  cs = counts_of_iterable(c for c in base if c.isalpha())

  top_5 = sorted(cs.items(), key=lambda x: (-x[1], x[0]))[:5]

  if ''.join(c for c,_ in top_5) == check_sum:
    return True

  return False

def get_key(code):
  return int(''.join(c for c in code if c.isnumeric()))

def main(raw, part):
  data = processInput(raw)

  if part == 1:
    return sum(get_key(c) for c in data if is_real(c))
  elif part == 2:
    for name in data:
      if is_real(name):
        print(caesar_str(name, get_key(name)))
    return 0

if __name__ == '__main__':
  part1_sample = main(readFileName('s.txt'), 1)
  print('Part 1 (sample):', part1_sample)
  assert part1_sample == 1514

  part1_real = main(readFileName('r.txt'), 1)
  print('Part 1 (real):', part1_real)
  assert part1_real == 173787

  part2_sample = main(readFileName('s.txt'), 2)
  print('Part 2 (sample):', part2_sample)
  assert part2_sample == 0

  part2_real = main(readFileName('r.txt'), 2)
  print('Part 2 (real):', part2_real)
  # assert part2_real == 0
