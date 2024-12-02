from utils import *
import re

GRID = [[1,2,3], [4,5,6], [7,8,9]]
DRNS = { 'U': (-1, 0), 'L': (0, -1), 'D': (1, 0), 'R': (0, 1) }

_ = None
GRID2 = [[_, _, 1, _, _], [_, 2, 3, 4, _], [5, 6, 7, 8, 9], [_, 'A', 'B', 'C', _], [_, _, 'D', _, _]]

def processInput(data):
  out = []

  for line in data:
    out.append(line)

  return out

def process(instrs, grid, start):
  pos = start
  seq = ''

  for row in instrs:
    for c in row:
      after = tadd(pos, DRNS[c])
      if inGrid(grid, *after) and grid[after[0]][after[1]] != None:
        pos = after
    #   print('Now at', grid[pos[0]][pos[1]])
    # print('-- Finalised')
    seq += str(grid[pos[0]][pos[1]])
  
  return seq

def main(raw, part):
  total = 0

  data = processInput(raw)

  if part == 1:
    return process(data, GRID, (1, 1))
  elif part == 2:
    return process(data, GRID2, (2, 0))

if __name__ == '__main__':
  part1_sample = main(readFileName('s.txt'), 1)
  print('Part 1 (sample):', part1_sample)
  assert part1_sample == '1985'

  part1_real = main(readFileName('r.txt'), 1)
  print('Part 1 (real):', part1_real)
  assert part1_real == '78985'

  part2_sample = main(readFileName('s.txt'), 2)
  print('Part 2 (sample):', part2_sample)
  assert part2_sample == '5DB3'

  part2_real = main(readFileName('r.txt'), 2)
  print('Part 2 (real):', part2_real)
  # assert part2_real == 0
