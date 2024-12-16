import sys
from collections import defaultdict, deque
from queue import PriorityQueue

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

def ttimes(a, f):
  return tuple(x*f for x in a)

def tadd(a, b):
  assert len(a) == len(b)
  return tuple(x+y for x,y in zip(a,b))

def tminus(a, b):
  assert len(a) == len(b)
  return tuple(x-y for x,y in zip(a,b))

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

def bfs3(graph, start, end, seen):
  if start == end:
    print('Found a path of length:', len(seen))
    yield len(seen)

  elif start in seen:
    yield 0

  else:
    seen.add(start)

    most = -1
    for neighbour,_ in graph[start]:
      if neighbour not in seen:
        for v in bfs3(graph, neighbour, end, seen):
          yield v
        # most = max(most, bfs3(graph, neighbour, end, seen))

    seen.remove(start)

    # return most

def bfs4(graph, start, end, seen, so_far):
  if start in seen:
    # yield 0
    return -1

  elif start == end:
    # print('Found a path of length:', len(seen))
    return so_far


  else:
    seen.add(start)

    most = -1
    for neighbour,l in graph[start]:
      # if neighbour not in seen:
      # for v in bfs4(graph, neighbour, end, seen, so_far + l):
        # most = max(most, v)
      most = max(most, bfs4(graph, neighbour, end, seen, so_far + l))

    seen.remove(start)

    return most

def bfs2(graph, start, is_finish_node):
  from_map = { start: (-1, -1) }
  best_to = {}
  queue = deque()
  queue.append((start, 0))
  found_end = None
  most_steps_to_end = 0

  while len(queue):
    current,steps = queue.popleft()

    if current in best_to and best_to[current] > steps:
      continue

    best_to[current] = steps

    if is_finish_node(current):
      most_steps_to_end = max(most_steps_to_end, steps)
      found_end = True

    for neighbour,_ in graph[current]:
      if neighbour in best_to and best_to[neighbour] > steps + 1:
        continue
      if from_map[current] == (neighbour, steps - 1):
        continue
      from_map[neighbour] = (current, steps)
      queue.append((neighbour, steps + 1))

  assert found_end
  # path = [found_end]

  # while path[-1] != start:
  #   path.append(from_map[path[-1]])

  return most_steps_to_end

def weightedBfs(graph, start, is_finish_node):
  from_map = {}
  seen = set()
  queue = PriorityQueue()
  queue.put((0, start))
  found_end = None

  while not queue.empty():
    dist,node = queue.get()

    if node in seen:
      continue

    seen.add(node)

    if is_finish_node(node):
      found_end = node
      break
    for neighbour,extraDist in graph[node]:
      tot = dist + extraDist
      if neighbour in from_map:
        if from_map[neighbour][1] <= tot:
          continue
      from_map[neighbour] = (node, tot)
      queue.put((tot, neighbour))

  assert found_end
  path = [found_end]

  while path[-1] != start:
    path.append(from_map[path[-1]][0])

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

def flood_fill_steps(graph, start, steps):
  from_map = {}
  seen = set()
  queue = deque()
  queue.append((start, 0))

  while len(queue):
    current, so_far = queue.popleft()

    if current in seen or so_far > steps:
      continue

    seen.add(current)

    for neighbour,_ in graph[current]:
      if neighbour in from_map:
        continue
      from_map[neighbour] = current
      queue.append((neighbour, so_far + 1))

  return seen, from_map

def flood_fill_all(graph, start, ends):
  results = {}
  seen = set()
  queue = deque()
  queue.append((start, 0))

  while len(queue):
    current, so_far = queue.popleft()

    if current in seen:
      continue

    seen.add(current)

    if current in ends and current != start:
      results[current] = max(results.get(current, 0), so_far)
      continue

    for neighbour,_ in graph[current]:
      if neighbour in seen:
        continue
      queue.append((neighbour, so_far + 1))

  return results

def flood_in_exactly(graph, start, steps):
  spots = set()
  spots.add(start)

  for i in range(steps):
    can_reach = set()

    for item in spots:
      for neighbour,_ in graph[item]:
        can_reach.add(neighbour)

    spots = can_reach

  return len(spots)

def wrap_into(grid, rc):
  r,c = rc
  return ((r + len(grid)) % len(grid), (c + len(grid[0])) % len(grid[0]))

def flatten(grid, rc):
  r,c = rc
  return ((r // len(grid)), (c // len(grid[0])))

def mhd(p1, p2):
  return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def flood_in_exactly2(graph2, start, steps, grid):
  spots = set()
  spots.add(start)
  simple_zones = set()
  zone_history = defaultdict(list)
  ls = [len(spots)]

  at_exactlies = defaultdict(list)

  for i in range(steps):
    # print(spots)
    # can_reach = defaultdict(int)
    s = set()

    for item in spots:
      # count = spots[item]
      for neighbour,_ in graph2(item):
        s.add(neighbour)

    zone_data = defaultdict(int)

    for item in s:
      zone = flatten(grid, item)
      if zone in simple_zones:
        continue

      zone_data[zone] += 1

    spots = set(x for x in s if flatten(grid, x) not in simple_zones)
    ls.append(len(spots))

    at_exactly = defaultdict(int)
    for x in spots:
      at_exactly[mhd(x, start)] += 1

    running = 0
    for k in range(i+1):
      running += at_exactly[k]
      at_exactlies[k].append(running)

    print(i+1, 'steps, considering', i-5, ':', at_exactlies[i-5][-4:])

  print('STEPS', steps, len(list((r,c) for r,c in spots if (abs(r-start[0]) + abs(c-start[1])) <= 65)))

  # return len(spots) + sum(zone_history[x][-1] for x in simple_zones)
  return ls

def grid_to_graph(grid, valid_move, allowDiag=True):
  return graph_maker(
    [rc for _,rc,__ in enumerateGrid(grid)],
    lambda rc: [(rc2, 1) for _,rc2 in walkNeighbours(grid, *rc, allowDiag=allowDiag) if valid_move(rc, rc2)]
  )

def wrapping_grid_to_graph(grid, check_chars, allowDiag):
  def edges_from(pos):
    r,c = pos
    out = []
    for r1 in range(-1, 2):
      for c1 in range(-1, 2):
        if r1 == 0 and c1 == 0:
          continue
        if not allowDiag and (r1 and c1):
          continue
        r2,c2 = (r+r1, c+c1)
        v1 = grid[r % len(grid)][c % len(grid[0])]
        v2 = grid[r2 % len(grid)][c2 % len(grid[0])]
        if check_chars(v1, v2):
          out.append(((r2,c2),1))
    return out
  return edges_from

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

def counts_of_iterable(iterable):
  counts = defaultdict(int)
  for i in iterable:
    counts[i] += 1

  return counts

def caesar_char(c, step):
  if not c.isalpha():
    return c

  step = ((step % 26) + 260) % 26

  base = ord('A') if c.isupper() else ord('a')

  inc = (ord(c) - base + step) % 26
  return chr(base + inc)

def caesar_str(string, step):
  return ''.join(caesar_char(c, step) for c in string)

def test(name, expected, actual):
  if expected == actual:
    print('PASS! {} got result: {}'.format(name, expected))
  else:
    print('FAIL! {} expected: {}, but got: {}'.format(name, expected, actual))
    print()
    assert expected == actual
