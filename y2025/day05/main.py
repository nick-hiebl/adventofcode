from utils import *
import re

def processInput(data):
  ranges = []

  singles = []

  seen_blank = False

  for line in data:

    if seen_blank:
      singles.append(int(line))
    else:
      if not line:
        seen_blank = True
      else:
        ranges.append(tuple(map(int, line.split('-'))))


  return ranges, singles

def overlap(a, b):
  if a[0] <= b[1] and b[0] <= a[1]:
    return True
  return False

def main(raw, part):
  total = 0

  ranges, singles = processInput(raw)

  if part == 1:
    for ing in singles:
      if any(a <= ing <= b for a,b in ranges):
        total += 1
    return total
  elif part == 2:
    while True:
      any_overlaps = False
      new_ranges = []

      for range1 in ranges:
        found_overlap = False
        for r2 in new_ranges:
          if overlap(range1, r2):
            new_ranges.remove(r2)
            new_ranges.append((min(range1[0], r2[0]), max(range1[1], r2[1])))
            found_overlap = True
            any_overlaps = True
        if not found_overlap:
          new_ranges.append(range1)
      
      ranges = new_ranges
      if not any_overlaps:
        break

    for a,b in ranges:
      total += b - a + 1

    return total

if __name__ == '__main__':
  test('p1 s1', 3, main(readFileName('s.txt'), 1))
  test('p1 real', 638, main(readFileName('r.txt'), 1))
  test('p2 s1', 14, main(readFileName('s.txt'), 2))
  test('p2 real', 0, main(readFileName('r.txt'), 2))
