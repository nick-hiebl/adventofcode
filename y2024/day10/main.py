from utils import *
import re

def processInput(data):
  def valid_move(rc1, rc2):
    r1,c1 = rc1
    r2,c2 = rc2
    v1 = data[r1][c1]
    v2 = data[r2][c2]

    return (int(v2) - int(v1)) == 1

  g = grid_to_graph(data, valid_move, False)

  return g

def dfs_all(graph, start, raw):
  r,c = start
  if raw[r][c] == '9':
    return 1
  
  return sum(dfs_all(graph, neighbour, raw) for neighbour, _ in graph[start])

def main(raw, part):
  total = 0

  grid = processInput(raw)

  if part == 1:
    for r, row in enumerate(raw):
      for c, cell in enumerate(row):
        if cell == '0':
          # Trailhead
          seen, from_map = flood_fill(grid, (r, c))

          score = 0
          for r1,c1 in seen:
            if raw[r1][c1] == '9':
              score += 1

          total += score

    # g = [['X' if (r,c) in path else cell for c,cell in enumerate(row)] for r,row in enumerate(raw)]
    # printGrid(g)
    return total
  elif part == 2:
    for r, row in enumerate(raw):
      for c, cell in enumerate(row):
        if cell == '0':
          # Trailhead
          total += dfs_all(grid, (r, c), raw)
    return total

if __name__ == '__main__':
  part1_sample = main(readFileName('s.txt'), 1)
  print('Part 1 (sample):', part1_sample)
  assert part1_sample == 36

  part1_real = main(readFileName('r.txt'), 1)
  print('Part 1 (real):', part1_real)
  assert part1_real == 617

  part2_sample = main(readFileName('s.txt'), 2)
  print('Part 2 (sample):', part2_sample)
  assert part2_sample == 81

  part2_real = main(readFileName('r.txt'), 2)
  print('Part 2 (real):', part2_real)
  # assert part2_real == 0
