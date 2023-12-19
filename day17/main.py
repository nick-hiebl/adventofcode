from utils import *
import re

def processInput(data):
  out = []

  for line in data:
    out.append(list(int(x) for x in line))

  return out

RIGHT = (0, 1)
LEFT = (0, -1)
UP = (-1, 0)
DOWN = (1, 0)

drns = [RIGHT, LEFT, UP, DOWN]

def solve(grid):
  graph = make_graph(grid)

  res = weightedBfs(graph, ((0,0), UP), lambda x: x[0] == (len(grid)-1, len(grid[-1])-1))
  print(res)
  c = 0
  for a,b in zip(res, res[1:]):
    edge = [x for x in graph[a] if x[0] == b][0]
    c += edge[1]
  return c

def is_inside(grid, rc):
  r,c = rc
  return 0 <= r < len(grid) and 0 <= c < len(grid[r])

def make_graph(grid):
  END = (len(grid)-1, len(grid[-1])-1)
  graph = {}
  for x, rc, row in enumerateGrid(grid):
    for bannedDrn in drns:
      edges = []
      graph[(rc,bannedDrn)] = edges
      for nextDrn in drns:
        if bannedDrn == nextDrn or bannedDrn == tminus((0,0), nextDrn):
          continue
        pos = rc
        c = 0
        for i in range(1, 11):
          canTurn = 4 <= i and i <= 10
          pos = tadd(pos, nextDrn)
          if not is_inside(grid, pos):
            break
          c += grid[pos[0]][pos[1]]
          if canTurn:
            edges.append(((pos,nextDrn), c))
          # elif pos == END:
          #   edges.append(((pos,UP), c))
  return graph

def main(raw, part):
  total = 0

  data = processInput(raw)
  # print(data)

  if part == 1 or part == 2:
    return solve(data)
  elif part == 2:
    for cmd in data:
      pass
    return total

if __name__ == '__main__':
  # part1_sample = main(readFileName('s.txt'), 1)
  # print('Part 1 (sample):', part1_sample)
  # assert part1_sample == 102

  # part1_real = main(readFileName('r.txt'), 1)
  # print('Part 1 (real):', part1_real)
  # assert part1_real == 722

  part2_sample = main(readFileName('s.txt'), 2)
  print('Part 2 (sample):', part2_sample)
  assert part2_sample == 94

  part2_sample = main(readFileName('s2.txt'), 2)
  print('Part 2 (sample 2):', part2_sample)
  assert part2_sample == 71

  part2_real = main(readFileName('r.txt'), 2)
  print('Part 2 (real):', part2_real)
  # assert part2_real == 0
