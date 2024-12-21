from utils import *
import re
import sys

sys.setrecursionlimit(10**6)

def processInput(data):
  end = tuple()
  start = tuple()

  for r, row in enumerate(data):
    if 'E' in row:
      end = (r, row.index('E'))
    if 'S' in row:
      start = (r, row.index('S'))

  def is_valid_move(rc1, rc2):
    return data[rc1[0]][rc1[1]] in ('S', '.', 'E') and data[rc2[0]][rc2[1]] in ('S', '.', 'E')

  graph = grid_to_graph(data, is_valid_move, False)

  return graph, start, end

def fill_distances(current, distances, from_map):
  if current in distances:
    return
  
  prior = from_map[current]

  if prior not in distances:
    fill_distances(prior, distances, from_map)
  
  distances[current] = distances[prior] + 1

def all_distances(graph, start):
  seen, from_map = flood_fill(graph, start)
  dist = {}

  dist[start] = 0

  for node in seen:
    fill_distances(node, dist, from_map)

  return dist

def manhattan(a, b):
  return abs(a[0] - b[0]) + abs(a[1] - b[1])

def main(raw, part, real):
  total = 0

  raw = [list(r) for r in raw]
  graph, start, end = processInput(raw)

  can_skip_through = 2 if part == 1 else 20
  must_beat = 100 if real else (20 if part == 1 else 70)

  default_path = bfs(graph, start, lambda x: x == end)
  normal = len(default_path)

  ds = all_distances(graph, start)
  es = all_distances(graph, end)

  for start_skip in ds:
    for end_skip in es:
      if manhattan(start_skip, end_skip) <= can_skip_through:
        if ds[start_skip] + es[end_skip] + manhattan(start_skip, end_skip) <= normal - must_beat:
          total += 1

  return total

if __name__ == '__main__':
  test('p1 s1', 5, main(readFileName('s.txt'), 1, False))
  test('p1 real', 1351, main(readFileName('r.txt'), 1, True))
  test('p2 s1', 41, main(readFileName('s.txt'), 2, False))
  test('p2 real', 966130, main(readFileName('r.txt'), 2, True))
