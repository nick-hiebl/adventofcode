from utils import *
import re

def processInput(data):
  out = []

  for line in data:
    d, c, col = line.split(' ')
    out.append((d, int(c)))

  return out

def process2(data):
  out = []

  for line in data:
    v = line.split(' ')[2]
    l = int(v[2:7], 16)
    d = 'RDLU'[int(v[7])]

    out.append((d, l))
  return out

maps = {
  'R': (0, 1),
  'U': (-1, 0),
  'L': (0, -1),
  'D': (1, 0),
}

def getBounds(data):
  maxR = 0
  minR = 0
  maxC = 0
  minC = 0
  pos = (0, 0)
  for drn, l in data:
    pos = tadd(pos, ttimes(maps[drn], l))
    maxR = max(maxR, pos[0])
    minR = min(minR, pos[0])
    maxC = max(maxC, pos[1])
    minC = min(minC, pos[1])

  print('r', minR, maxR, 'c', minC, maxC)
  return (minR, maxR), (minC, maxC)

def makeGrid(data):
  rs,cs = getBounds(data)
  minR,maxR = rs
  minC, maxC = cs
  pos = (-minR,-minC)
  h = maxR - minR + 1
  w = maxC - minC + 1

  g = [['.' for i in range(w)] for j in range(h)]

  for drn, l in data:
    v = maps[drn]
    for i in range(l):
      g[pos[0]][pos[1]] = '#'
      pos = tadd(pos, v)
  g[pos[0]][pos[1]] = '#'

  printGrid(g)
  return g

def calculateArea(data):
  pos = (0, 0)
  ps = [pos]
  for drn, l in data:
    print(drn, l)
    pos = tadd(pos, ttimes(maps[drn], l))
    ps.append(pos)
  print(ps)
  
  iArea = 0

  for p1, p2 in list(zip(ps, ps[1:])) + [(ps[-1], ps[0])]:
    iArea += (p1[0] * p2[1] - p2[0] * p1[1])

  insideArea = abs(iArea // 2)

  edgePath = ''.join(x[0] for x in data) + data[0][0]
  print('EDGEPATH', edgePath)
  edgeArea = 1/2 * sum(l for d,l in data)
  outCorners = sum(edgePath.count(corner) for corner in ['RD', 'DL', 'LU', 'UR'])
  inCorners = sum(edgePath.count(corner) for corner in ['DR', 'LD', 'UL', 'RU'])
  print('OUT IN', outCorners, inCorners)

  cornerArea = (1/4) * (outCorners - inCorners)

  print('MY SPECIAL RESULT >>>', edgeArea, cornerArea, edgeArea + insideArea + cornerArea)
  return insideArea + edgeArea + cornerArea

def main(raw, part, insidePoint=(0,0)):
  total = 0

  data = processInput(raw)

  if part == 1:
    return calculateArea(data)
    g = makeGrid(data)
    graph = grid_to_graph(g, lambda rc1, rc2: g[rc2[0]][rc2[1]] == '.', False)
    seen, froms = flood_fill(graph, insidePoint)
    edges = sum(sum(1 if x == '#' else 0 for x in row) for row in g)
    innies = len(seen)
    print('Edges', edges, 'Innies', innies)
    return edges + innies
  elif part == 2:
    data = process2(raw)
    return calculateArea(data)

if __name__ == '__main__':
  part1_sample = main(readFileName('s.txt'), 1, (1,1))
  print('Part 1 (sample):', part1_sample)
  assert part1_sample == 62

  part1_real = main(readFileName('r.txt'), 1, (19,94))
  print('Part 1 (real):', part1_real)
  assert part1_real == 35244

  part2_sample = main(readFileName('s.txt'), 2)
  print('Part 2 (sample):', part2_sample)
  assert part2_sample == 952408144115.0

  part2_real = main(readFileName('r.txt'), 2)
  print('Part 2 (real):', part2_real)
  # assert part2_real == 0
