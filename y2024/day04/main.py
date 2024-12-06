from utils import *
import re

def processInput(data):
  out = []

  for line in data:
    out.append(line)

  return out

def rot(data):
  return [''.join(x) for x in zip(*data)]

def shift(data):
  w = len(data[0])
  h = len(data)

  rows = []
  for i in range(w + h - 1):
    row = ''
    # print('new')
    for j in range(1000):
      r = j
      c = w - i - 1 + j
      if c >= w or r >= h:
        break
      if c >= 0 and h >= 0:
        row += data[r][c]
    #   print(r, c)
    # print(row)
    rows.append(row)
  return rows

def check_group(ds):
  if ds[2] != 'A':
    return False
  if ds.count('M') == 2 and ds.count('S') == 2 and ds[0] != ds[4]:
    return True
  return False

def main(raw, part):
  total = 0

  data = processInput(raw)

  if part == 1:
    for line in data:
      found = line.count('XMAS') + line.count('SAMX')
      total += found
    for line in rot(data):
      found = line.count('XMAS') + line.count('SAMX')
      total += found
    for line in shift(data):
      found = line.count('XMAS') + line.count('SAMX')
      total += found
    for line in shift(data[::-1]):
      found = line.count('XMAS') + line.count('SAMX')
      total += found
    
    return total
  elif part == 2:
    for r, row in enumerate(data):
      if r >= len(data) - 2:
        break
      for c, col in enumerate(row):
        if c >= len(row) - 2:
          break
        group = [data[r][c], data[r][c+2], data[r+1][c+1], data[r+2][c], data[r+2][c+2]]
        if check_group(group):
          total += 1
    return total

if __name__ == '__main__':
  part1_sample = main(readFileName('s.txt'), 1)
  print('Part 1 (sample):', part1_sample)
  assert part1_sample == 18

  part1_real = main(readFileName('r.txt'), 1)
  print('Part 1 (real):', part1_real)
  assert part1_real == 2575

  part2_sample = main(readFileName('s2.txt'), 2)
  print('Part 2 (sample):', part2_sample)
  assert part2_sample == 9

  part2_real = main(readFileName('r.txt'), 2)
  print('Part 2 (real):', part2_real)
  # assert part2_real == 0
