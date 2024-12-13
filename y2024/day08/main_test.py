from utils import *
import re

def processInput(data):
  def valid_move(rc1, rc2):
    r1,c1 = rc1
    r2,c2 = rc2
    v1 = data[r1][c1]
    v2 = data[r2][c2]

    return v1 in ['.'] and v2 in ['.']

  g = grid_to_graph(data, valid_move, False)

  return g

def main(raw, part):
  total = 0

  grid = processInput(raw)

  if part == 1:
    path = bfs(grid, (0, 0), lambda rc: rc[0] == len(raw) - 1 and rc[1] == len(raw[0]) - 1)
    p = set(path)

    g = [['X' if (r,c) in path else cell for c,cell in enumerate(row)] for r,row in enumerate(raw)]
    printGrid(g)
    return path
  elif part == 2:
    for cmd in data:
      pass
    return total

if __name__ == '__main__':
  part1_sample = main(readFileName('s.txt'), 1)
  print('Part 1 (sample):', part1_sample)
  assert part1_sample == 0

  part1_real = main(readFileName('r.txt'), 1)
  print('Part 1 (real):', part1_real)
  assert part1_real == 0

  part2_sample = main(readFileName('s.txt'), 2)
  print('Part 2 (sample):', part2_sample)
  assert part2_sample == 0

  part2_real = main(readFileName('r.txt'), 2)
  print('Part 2 (real):', part2_real)
  # assert part2_real == 0
