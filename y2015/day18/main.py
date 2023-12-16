from utils import *
import re

def processInput(data):
  out = [[1 if x == '#' else 0 for x in row] for row in data]
  # Kinda gave up on pt-1, pt-2ing this and just chucked this in breaking pt 1
  out[0][0] = 1
  out[0][-1] = 1
  out[-1][0] = 1
  out[-1][-1] = 1
  return out

def step(grid):
  out = [[0] * len(row) for row in grid]
  # Kinda gave up on pt-1, pt-2ing this and just chucked this in breaking pt 1
  out[0][0] = 1
  out[0][-1] = 1
  out[-1][0] = 1
  out[-1][-1] = 1
  for v, pos, row in enumerateGrid(grid):
    ns = 0
    for v2,xy in walkNeighbours(grid, *pos):
      ns += v2
    if v:
      if ns in (2,3):
        out[pos[0]][pos[1]] = 1
    else:
      if ns == 3:
        out[pos[0]][pos[1]] = 1
  return out

def main(raw, part):
  total = 0

  data = processInput(raw)

  if part == 1:  
    printGrid(data, lambda x: '#' if x else '.', '')
    for i in range(100):
      data = step(data)
      printGrid(data, lambda x: '#' if x else '.', '')
    return sum(map(sum, data))
  elif part == 2:
    for cmd in data:
      pass
    return total

if __name__ == '__main__':
  # Broke pt 1 (see lines 6 and 15), this just does pt 2 now

  # part1_sample = main(readFileName('s.txt'), 1)
  # print('Part 1 (sample):', part1_sample)
  # # assert part1_sample == 4

  part1_real = main(readFileName('r.txt'), 1)
  print('Part 1 (real):', part1_real)
  assert part1_real == 0

  # part2_sample = main(readFileName('s.txt'), 2)
  # print('Part 2 (sample):', part2_sample)
  # assert part2_sample == 0

  # part2_real = main(readFileName('r.txt'), 2)
  # print('Part 2 (real):', part2_real)
  # # assert part2_real == 0
