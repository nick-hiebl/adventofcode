from utils import *
import re
from collections import *

sys.setrecursionlimit(50000)

def processInput(data):
  out = []

  for line in data:
    out.append(line)

  return out

def main(raw, part):
  total = 0

  data = [list(x) for x in processInput(raw)]

  def valid_move(rc1, rc2):
    r1,c1 = rc1
    r2,c2 = rc2
    v1 = data[r1][c1]
    v2 = data[r2][c2]

    if v1 == '#' or v2 == '#':
      return False
    if part == 1 and v1 in ('<', '>', '^', 'v'):
      shape = { '<': (0, -1), '>': (0, 1), '^': (-1, 0), 'v': (1, 0) }
      # print('On:', v1, 'going', rc1, rc2, tminus(rc2, rc1) == shape[v1])
      return tminus(rc2, rc1) == shape[v1]
    return True

  g = grid_to_graph(data, valid_move, False)

  start = (0, 1)
  end = (len(data) - 1, len(data[0]) - 2)
  if part == 1:
    path = bfs2(g, start, lambda x: x == end)
    # print(path)
    # for v, rc, row in enumerateGrid(data):
    #   if rc in path and v == '.':
    #     row[rc[1]] = 'O'
    # printGrid(data)
    return path
  elif part == 2:
    big_nodes = set()
    big_nodes.add(start)
    big_nodes.add(end)
    for node in g:
      if len(g[node]) > 2:
        big_nodes.add(node)
    
    print(flood_fill_all(g, start, big_nodes))

    g2 = {}

    names = { start: 'start', end: 'end' }

    i = 1

    for n in big_nodes:
      res = flood_fill_all(g, n, big_nodes)
      g2[n] = list((x, res[x]) for x in res.keys())
      i += 1
      if n not in names:
        names[n] = 'a' + str(i)

    print(g2)
    print(len(big_nodes))

    # for n in names:
    #   for neighbour,_ in g2[n]:
    #     if names[n] < names[neighbour]:
    #       print(names[n], '->', names[neighbour])

    # for n in names:
    #   print(names[n], ':', list((names[x], c) for x,c in g2[n]))

    # return 0

    x = 0
    for l in bfs4(g, start, end, set(), 0):
      if l > x:
        print('New best:', l)
      x = max(l, x)
      print('Got out:', l, x)
    return x

    count = 0
    ans = 0
    SEEN = set()
    def dfs6(node, dist):
      nonlocal count
      nonlocal ans
      count += 1
      if node in SEEN:
        return
      SEEN.add(node)
      if node == end:
        if dist > ans:
          print('Comping', ans, dist)
        ans = max(ans, dist)
      for neighbour,cost in g2[node]:
        dfs6(neighbour, dist + cost)
      SEEN.remove(node)
      # print(count)
    dfs6(start, 0)
    return ans
    # return x

if __name__ == '__main__':
  # part1_sample = main(readFileName('s.txt'), 1)
  # print('Part 1 (sample):', part1_sample)
  # assert part1_sample == 94

  # part1_real = main(readFileName('r.txt'), 1)
  # print('Part 1 (real):', part1_real)
  # assert part1_real == 2030

  # part2_sample = main(readFileName('s.txt'), 2)
  # print('Part 2 (sample):', part2_sample)
  # assert part2_sample == 154

  part2_real = main(readFileName('r.txt'), 2)
  print('Part 2 (real):', part2_real)
  # assert part2_real == 0
