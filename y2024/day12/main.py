from utils import *
import re

def processInput(data):
  out = []

  for line in data:
    out.append(line)

  def valid_move(rc1, rc2):
    r1,c1 = rc1
    r2,c2 = rc2
    v1 = data[r1][c1]
    v2 = data[r2][c2]

    return v1 == v2
  
  def valid_all(rc1, rc2):
    return True

  g = grid_to_graph(data, valid_move, False)
  g2 = grid_to_graph(data, valid_all, False)

  return out, g, g2

def perimeter(region, g):
  p = 0
  for cell in region:
    # print(cell, g[cell])
    for neighbour,w in g[cell]:
      if neighbour not in region:
        p += 1
    p += 4 - len(g[cell])
  return p

def is_fence(ab):
  return ab[0] != ab[1]

def perimeter2(region):
  min_r = min(r for r,_ in region)
  max_r = max(r for r,_ in region)
  min_c = min(c for _,c in region)
  max_c = max(c for _,c in region)

  fences = 0

  for r in range(min_r-1, max_r + 1):
    last_fence = (False, False)
    for c in range(min_c, max_c + 1):
      fence_dir = ((r,c) in region, (r+1,c) in region)
      is_edge = ((r,c) in region) != ((r+1,c) in region)

      if is_fence(fence_dir) and fence_dir != last_fence:
        fences += 1

      last_fence = fence_dir

  for c in range(min_c-1, max_c + 1):
    last_fence = (False, False)
    for r in range(min_r, max_r + 1):
      fence_dir = ((r,c) in region), ((r,c+1) in region)

      if is_fence(fence_dir) and fence_dir != last_fence:
        fences += 1

      last_fence = fence_dir
  
  return fences


def main(raw, part):
  total = 0

  data, graph, neighs = processInput(raw)

  regions = []
  seen_ever = set()

  if part == 1:
    for r, row in enumerate(data):
      for c, cell in enumerate(row):
        rc = (r, c)
        if rc in seen_ever:
          continue
        region, _ = flood_fill(graph, rc)

        regions.append(region)

        for v in region:
          seen_ever.add(v)

    for region in regions:
      area = len(region)
      prm = perimeter(region, neighs)
      l = list(region)
      # print(l, l[0])
      # base = l[0]
      # print(data[l[0][0]][l[0][1]], area, prm)

      total += area * prm

    return total
  elif part == 2:
    for r, row in enumerate(data):
      for c, cell in enumerate(row):
        rc = (r, c)
        if rc in seen_ever:
          continue
        region, _ = flood_fill(graph, rc)

        regions.append(region)

        for v in region:
          seen_ever.add(v)

    for region in regions:
      area = len(region)
      prm = perimeter2(region)
      l = list(region)
      # print(l, l[0])
      base = l[0]
      print(data[base[0]][base[1]], area, prm)

      total += area * prm
    return total

if __name__ == '__main__':
  # part1_sample = main(readFileName('s.txt'), 1)
  # print('Part 1 (sample):', part1_sample)
  # assert part1_sample == 140

  # part1_real = main(readFileName('r.txt'), 1)
  # print('Part 1 (real):', part1_real)
  # assert part1_real == 1573474

  part2_sample = main(readFileName('s.txt'), 2)
  print('Part 2 (sample):', part2_sample)
  assert part2_sample == 80

  part2_sample2 = main(readFileName('s2.txt'), 2)
  print('Part 2 (sample):', part2_sample2)
  assert part2_sample2 == 1206

  part2_sample3 = main(readFileName('s3.txt'), 2)
  print('Part 2 (sample):', part2_sample3)
  assert part2_sample3 == 236

  part2_sample4 = main(readFileName('s4.txt'), 2)
  print('Part 2 (sample):', part2_sample4)
  assert part2_sample4 == 368

  part2_real = main(readFileName('r.txt'), 2)
  print('Part 2 (real):', part2_real)
  # assert part2_real == 0
