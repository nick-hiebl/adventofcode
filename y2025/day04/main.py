from utils import *
import re

def processInput(data):
  out = []

  for line in data:
    out.append(line)

  return out

def main(raw, part):
  total = 0

  data = [list(row) for row in raw]

  if part == 1:
    print('\n'.join([''.join(row) for row in data]))
    for r, row in enumerate(data):
      for c, col in enumerate(row):
        if col != '@':
          continue

        rolls = 0

        for v, coord in walkNeighbours(data, r, c):
          if v == '@':
            rolls += 1

        if rolls < 4:
          total += 1
    return total
  elif part == 2:
    while True:
      some_progress = False

      for r, row in enumerate(data):
        for c, col in enumerate(row):
          if col != '@':
            continue

          rolls = 0

          for v, coord in walkNeighbours(data, r, c):
            if v == '@':
              rolls += 1

          if rolls < 4:
            data[r][c] = '.'
            some_progress = True
            total += 1
      
      if not some_progress:
        break

    return total

if __name__ == '__main__':
  test('p1 s1', 13, main(readFileName('s.txt'), 1))
  test('p1 real', 1363, main(readFileName('r.txt'), 1))
  test('p2 s1', 43, main(readFileName('s.txt'), 2))
  test('p2 real', 0, main(readFileName('r.txt'), 2))
