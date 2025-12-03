from utils import *
import re

def processInput(data):
  out = []

  for pair in data[0].split(','):
    lo, hi = map(int, pair.split('-'))
    out.append((lo, hi))

  return out

def overlaps(a, b, x, y):
  return b >= x and a <= y

def get_group(base, max_multi):
  return range(base, base * max_multi + 1, base)

def iterate_all_doubles():
  i = 1
  while True:
    i *= 10

    base = i + 1

    for j in range(i // 10, i):
      yield base * j

def iterate_all_megas(max_size):
  i = 1
  while True:
    i *= 10

    base = i + 1

    if base > max_size:
      break

    mega = base

    while mega < max_size:
      for j in range(i // 10, i):
        if mega * j > max_size:
          break
        yield mega * j
      
      mega = mega * i + 1

def main(raw, part):
  data = processInput(raw)

  big_boy = 0

  all_nums = 0

  for cmd in data:
    big_boy = max(cmd[0], cmd[1], big_boy)
    all_nums += cmd[1] - cmd[0] + 1

  total = 0

  print('All numbers', all_nums)

  if part == 1:
    for v in iterate_all_doubles():
      if v > big_boy:
        break
      if any(v >= low and v <= high for low, high in data):
        total += v

    return total
  elif part == 2:
    nums_considered = 0
    seen = set()
    for v in iterate_all_megas(big_boy):
      nums_considered += 1
      if any(v >= low and v <= high for low, high in data):
        if v not in seen:
          total += v
          seen.add(v)

    print('WIDTH', all_nums, 'PROBLEMS', nums_considered)

    return total

if __name__ == '__main__':
  test('p1 s1', 1227775554, main(readFileName('s.txt'), 1))
  test('p1 real', 19128774598, main(readFileName('r.txt'), 1))
  test('p2 s1', 4174379265, main(readFileName('s.txt'), 2))
  test('p2 real', 21932258645, main(readFileName('r.txt'), 2))
