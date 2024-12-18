from utils import *
import re
import networkx

DIRNS = [
  (1, 0),
  (0, 1),
  (-1, 0),
  (0, -1),
]

def processInput(data):
  graph = networkx.DiGraph()

  spots = set()
  start = tuple()
  end = tuple()

  for r, row in enumerate(data):
    for c, cell in enumerate(row):
      if cell == 'S':
        start = (r, c)
      elif cell == 'E':
        end = (r, c)

      if cell in ('.', 'S', 'E'):
        spots.add((r, c))

  for spot in spots:
    for dirn in DIRNS:
      if tadd(spot, dirn) in spots:
        graph.add_edge((spot, dirn), ((tadd(spot, dirn), dirn)), weight=1)

    for i,dirn in enumerate(DIRNS):
      graph.add_edge((spot, dirn), (spot, DIRNS[(i+1) % len(DIRNS)]), weight=1000)
      graph.add_edge((spot, dirn), (spot, DIRNS[(i+len(DIRNS) - 1) % len(DIRNS)]), weight=1000)

  return start, end, graph

def find_shortest_length(graph, start, end, raw):
  total = 0
  best_dir = []
  for end_dir in DIRNS:
    path = networkx.shortest_path(graph, (start,(0,1)), (end,end_dir), weight='weight')
    edges = list(zip(path, path[1:]))

    t = 0
    for a,b in edges:
      if a[0] == b[0]:
        t += 1000
      else:
        t += 1

    if total == 0:
      total = t
      best_path = path
      best_dir = [end_dir]
    elif t < total:
      total = t
      best_path = path
      best_dir = [end_dir]
    elif t == total:
      best_dir += [end_dir]
  
  shape = [list(row) for row in raw]
  for p,_ in best_path:
    r,c = p
    shape[r][c] = 'X'

  return total, best_dir

def main(raw, part):
  total = 0

  start, end, graph = processInput(raw)

  if part == 1:
    return find_shortest_length(graph, start, end, raw)[0]
  elif part == 2:
    d, end_dirs = find_shortest_length(graph, start, end, raw)
    spaces = set()

    for end_dir in end_dirs:
      for path in networkx.all_shortest_paths(graph, (start,(0,1)), (end,end_dir), weight='weight'):
        for p,d in path:
          spaces.add(p)
    return len(spaces)

if __name__ == '__main__':
  test('p1 s1', 7036, main(readFileName('s.txt'), 1))
  test('p1 real', 123540, main(readFileName('r.txt'), 1))
  test('p2 s1', 45, main(readFileName('s.txt'), 2))
  test('p2 real', 665, main(readFileName('r.txt'), 2))
