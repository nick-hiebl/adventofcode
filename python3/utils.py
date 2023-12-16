import sys
from collections import deque

def readFile():
  with open(sys.argv[1], 'r') as f:
    lines = [l.strip() for l in f.readlines()]

  return lines

def readFileName(name):
  with open(name, 'r') as f:
    lines = [l.strip() for l in f.readlines()]

  return lines

def enumerateGrid(grid):
  for r,row in enumerate(grid):
    for c,val in enumerate(row):
      yield val, (r,c), row

def walkNeighbours(grid, r, c, allowDiag=True):
  for i in range(-1, 2):
    for j in range(-1, 2):
      if i == 0 and j == 0:
        continue
      if (not allowDiag) and (i and j):
        continue
      if r+i < 0 or r+i >= len(grid):
        continue
      if c+j < 0 or c+j >= len(grid[r+i]):
        continue
      yield grid[r+i][c+j], (r+i, c+j)

def inGrid(grid, r, c):
  return 0 <= r and r < len(grid) and 0 <= c and c < len(grid[r])

def tadd(a, b):
  assert len(a) == len(b)
  return tuple(x+y for x,y in zip(a,b))

# Assumes lo is valid, hi is invalid
def binarySearch(lo, hi, test_left):
  while lo < hi and lo + 1 < hi:
    mid = (lo + hi) // 2
    if test_left(mid):
      hi = mid
    else:
      lo = mid
  if test_left(lo):
    return lo + 1
  else:
    return lo
  return lo

def rangeFilter(r, f):
  rLo, rHi = r
  fLo, fHi = f

  if rHi <= fLo or fHi <= rLo:
    return None, [r]
  elif rLo >= fLo and rLo < fHi:
    if rHi > fHi:
      return (rLo, fHi), [(fHi, rHi)]
    else:
      return (rLo, rHi), []
  elif rHi >= fLo and rHi <= fHi:
    assert rLo < fLo
    return (fLo, rHi), [(rLo, fLo)]
  elif rLo < fLo and rHi > fHi:
    return (fLo, fHi), [(rLo, fLo), (fHi, rHi)]
  else:
    assert False

def bundle(l, size=2):
  return [l[i:i+size] for i in range(0, len(l), size)]

def graph_maker(nodes, edges_from_node):
  graph = {}
  for node in nodes:
    graph[node] = edges_from_node(node)
  
  return graph

def bfs(graph, start, is_finish_node):
  from_map = {}
  seen = set()
  queue = deque()
  queue.append(start)
  found_end = None

  while len(queue):
    current = queue.popleft()

    if current in seen:
      continue

    seen.add(current)

    if is_finish_node(current):
      found_end = current
      break
    
    for neighbour,_ in graph[current]:
      if neighbour in from_map:
        continue
      from_map[neighbour] = current
      queue.append(neighbour)

  assert found_end
  path = [found_end]

  while path[-1] != start:
    path.append(from_map[path[-1]])
  
  return path[::-1]

def flood_fill(graph, start):
  from_map = {}
  seen = set()
  queue = deque()
  queue.append(start)
  
  while len(queue):
    current = queue.popleft()

    if current in seen:
      continue

    seen.add(current)

    for neighbour,_ in graph[current]:
      if neighbour in from_map:
        continue
      from_map[neighbour] = current
      queue.append(neighbour)
  
  return seen, from_map

def grid_to_graph(grid, valid_move, allowDiag=True):
  return graph_maker(
    [rc for _,rc,__ in enumerateGrid(grid)],
    lambda rc: [(rc2, 1) for _,rc2 in walkNeighbours(grid, *rc, allowDiag) if valid_move(rc, rc2)]
  )

def detectCycle(initial, step, cycles):
  seen = {}
  seen[initial] = 0
  s = initial
  for i in range(1, cycles):
    s = step(s)
    if s in seen:
      last = seen[s]
      now = i
      loop = now - last
      for j in range((cycles - last) % loop):
        s = step(s)
      return s
    seen[s] = i

def printGrid(grid, fn=str, rowConn = ''):
  print('\n'.join(rowConn.join(fn(x) for x in row) for row in grid), '\n')
