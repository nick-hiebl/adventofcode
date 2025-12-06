from utils import *
import re

def processInput(data):
  graph = weighted_grid_to_graph(data, lambda _,__: True, lambda _,rc: 1 if data[rc[0]][rc[1]] == '@' else 0, False)
  return graph

def main(raw, part):
  total = 0

  graph = processInput(raw)

  if part == 1:
    p = weightedBfs(graph, (0, 0), lambda rc: rc == (len(raw) - 1, len(raw[0]) - 1))

    cells = [raw[rc[0]][rc[1]] for rc in p]

    for r,c in p:
      raw[r] = string_replace_index(raw[r], c, 'X')

    printGrid(raw)

    return cells.count('@')
  elif part == 2:
    for cmd in data:
      pass
    return total

if __name__ == '__main__':
  test('p1 s1', 8, main(readFileName('s.txt'), 1))
  test('p1 real', 0, main(readFileName('r.txt'), 1))
  test('p2 s1', 0, main(readFileName('s.txt'), 2))
  test('p2 real', 0, main(readFileName('r.txt'), 2))
