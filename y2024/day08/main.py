from utils import *
import re
from collections import defaultdict
from itertools import permutations

def processInput(data):
  locations = defaultdict(list)
  maps = {}

  for r, row in enumerate(data):
    for c, char in enumerate(row):
      if char.isalnum():
        locations[char].append((r, c))
        maps[(r, c)] = char

  return locations, maps, data

def main(raw, part):
  total = 0

  locations, maps, grid = processInput(raw)
  spots = set()

  if part == 1:
    for shape in locations:
      for a,b in permutations(locations[shape], 2):
        diff = tminus(a, b)
        anti = tadd(a, diff)
        # print(shape, a, b, anti)
        assert anti != b
        # if anti in maps and maps[anti] != shape:
        if inGrid(grid, *anti):
          spots.add(anti)

    return len(spots)
  elif part == 2:
    for shape in locations:
      for a in locations[shape]:
        spots.add(a)
      for a,b in permutations(locations[shape], 2):
        diff = tminus(a, b)
        anti = tadd(a, diff)
        spots.add(a)
        spots.add(b)

        # if anti in maps and maps[anti] != shape:
        while inGrid(grid, *anti):
          # if anti in maps:
          #   break
          spots.add(anti)
          anti = tadd(anti, diff)
    
    out = [list(s) for s in grid]
    for spot in spots:
      out[spot[0]][spot[1]] = '#'
    printGrid(out)

    return len(spots)

if __name__ == '__main__':
  part1_sample = main(readFileName('s.txt'), 1)
  print('Part 1 (sample):', part1_sample)
  assert part1_sample == 14

  part1_real = main(readFileName('r.txt'), 1)
  print('Part 1 (real):', part1_real)
  assert part1_real == 265

  part2_sample2 = main(readFileName('s2.txt'), 2)
  print('Part 2 (sample):', part2_sample2)
  assert part2_sample2 == 9

  part2_sample = main(readFileName('s.txt'), 2)
  print('Part 2 (sample):', part2_sample)
  assert part2_sample == 34

  part2_real = main(readFileName('r.txt'), 2)
  print('Part 2 (real):', part2_real)
  # assert part2_real == 0
