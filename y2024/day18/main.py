from utils import *
import re

def processInput(data):
  out = []

  for line in data:
    a,b = map(int, line.split(','))
    out.append((b,a))

  return out

def is_possible(points, num, grid, end):
  pointset = set(points[:num])
  def valid_move(rc1, rc2):
    return (rc1 not in pointset) and (rc2 not in pointset)

  graph = grid_to_graph(grid, valid_move, False)

  try:
    bfs(graph, (0, 0), lambda x: x == end)
    return True
  except:
    return False

def main(raw, part, real):
  total = 0

  bounds = 71 if real else 7
  points = processInput(raw)
  end = (bounds-1, bounds-1)

  grid = [[False] * bounds for i in range(bounds)]

  if part == 1:
    pointset = set(points[:1024 if real else 12])
    def valid_move(rc1, rc2):
      return (rc1 not in pointset) and (rc2 not in pointset)

    graph = grid_to_graph(grid, valid_move, False)

    x = bfs(graph, (0, 0), lambda x: x == end)
    return len(x) - 1
  elif part == 2:
    last = 0
    invalid = binarySearch(0, len(points), lambda x: not is_possible(points, x, grid, end))
    invalid_point = points[invalid]

    return (invalid_point[1], invalid_point[0])

if __name__ == '__main__':
  test('Part 1 - sample', 22, main(readFileName('s.txt'), 1, False))
  test('Part 1 - real', 276, main(readFileName('r.txt'), 1, True))
  test('Part 2 - sample', (6, 1), main(readFileName('s.txt'), 2, False))
  test('Part 2 - real', (60, 37), main(readFileName('r.txt'), 2, True))
