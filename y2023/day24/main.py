from utils import *
import re
from itertools import combinations, permutations

def processInput(data):
  out = []

  for line in data:
    x,y = line.split(' @ ')
    a,b = tuple(map(int, x.split(', '))), tuple(map(int, y.split(', ')))

    out.append((a,b))

  return out

def det(a,b):
  return a[0] * b[1] - a[1] * b[0]

def inside(a, rng):
  return rng[0] <= a <= rng[1] or rng[1] <= a <= rng[0]

def same_dir(x, pos, vel):
  return (x - pos[0]) * vel[0] > 0

def pos_at(pos, vel, t):
  return tadd(pos, ttimes(vel, t))

def rock_to_hit(a, b, t1, t2):
  pa, va = a
  pb, vb = b
  collA = pos_at(pa, va, t1)
  collB = pos_at(pb, vb, t2)

  vel = ttimes(tminus(collB, collA), 1 / (t2 - t1))
  pos = tminus(collA, ttimes(vel, t1))

  return (pos,vel)

def intersect_at_2d(a, b):
  xa,ya,za,dxa,dya,dza = a
  xb,yb,zb,dxb,dyb,dzb = b

  ea = tadd((xa, ya, za), (dxa, dya, dza))
  eb = tadd((xb, yb, zb), (dxb, dyb, dzb))

  xdiff = (xa - ea[0], xb - eb[0])
  ydiff = (ya - ea[1], yb - eb[1])

  div = det(xdiff, ydiff)
  if div == 0:
    return None

  d = (det((xa,ya,za), ea), det((xb,yb,zb), eb))
  x = det(d, xdiff) / div
  y = det(d, ydiff) / div

  if not (same_dir(x, [xa], [dxa]) and same_dir(x, [xb], [dxb])):
    return None

  return (x,y)

def find_common_point(stones, vel):
  stones2 = [tminus(s, [0,0,0,*vel]) for s in stones]

  point_counts = defaultdict(int)

  last = intersect_at_2d(stones2[0], stones2[1])

  successes = 0
  i = 0
  if not last:
    # print(vel, 'Failed at 0')
    return False

  for a,b in zip(stones2, stones2[1:]):
    point = intersect_at_2d(a, b)
    if (not point):
      # print('No intersection???')
      pass

    point_counts[point] += 1
    # if (not point) or point != last:
    #   if i > 2:
    #     print(vel, 'Failed at', i, last, point, a, b)
    #   return False
    i += 1
    # successes += 1

  sxs = max(point_counts.values())
  # if sxs > 2:
  #   print(vel, 'got', sxs, 'matches out of', i)

  return sxs

def main(raw, part, lo, hi):
  total = 0

  data = processInput(raw)

  if part == 1:
    total = 0
    crashes = []
    for a,b in combinations(data, 2):
      # print(a, b)

      pa,va = a
      pb,vb = b
      ea = tadd(pa, ttimes(va, 1000 * abs(hi - lo)))
      eb = tadd(pb, ttimes(vb, 1000 * abs(hi - lo)))
      xdiff = (pa[0] - ea[0], pb[0] - eb[0])
      ydiff = (pa[1] - ea[1], pb[1] - eb[1])

      div = det(xdiff, ydiff)
      if div == 0:
        continue

      d = (det(pa, ea), det(pb, eb))
      x = det(d, xdiff) / div
      y = det(d, ydiff) / div

      # if (a in crashed and crashed[a] ) or b in crashed:
      #   print(a, b, 'already crashed', div)
      #   continue

      if lo <= x <= hi and lo <= y <= hi:
        # if not (inside(x, (pa[0], ea[0])) and inside(x, (pb[0], eb[0]))):
        if not (same_dir(x, pa, va) and same_dir(x, pb, vb)):
          print(x, 'outside', (pa[0], ea[0]), (pb[0], eb[0]))
          continue
        print(a,b, 'intersected at', (x,y), div)
        # crashed.add(a)
        # crashed.add(b)
        total += 1
        # crashes.append((div, a,b))

    # crashes.sort()

    # crashed = set()
    # for d, a, b in crashes:
    #   if a in crashed or b in crashed:
    #     continue
    #   crashed.add(a)
    #   crashed.add(b)
    #   total += 1

    return total
  elif part == 2:
    stones = [(x,y,z,dx,dy,dz) for (x,y,z),(dx,dy,dz) in data]

    costs = defaultdict(set)

    for stone in stones:
      vel_mag = sum(stone[i] ** 2 for i in range(3, 6)) ** 0.5

      costs[vel_mag].add(stone)

    # for k in sorted(costs.keys()):
    #   print(k, costs[k])
    # print(costs)

    bs = defaultdict(int)

    for rock_vx in range(-100, 101):
      for rock_vy in range(-100, 101):
        works = find_common_point(stones, (rock_vx, rock_vy, 0))
        bs[works] += 1
        # if works:
        #   print((rock_vx, rock_vy, 0))

    print('MOST MATCHES', max(bs.keys()))


    # total = 0
    # crashes = []
    # for a,b in combinations(data, 2):
    #   # print(a, b)

    #   pa,va = a
    #   pb,vb = b
    #   ea = tadd(pa, ttimes(va, 1000 * abs(hi - lo)))
    #   eb = tadd(pb, ttimes(vb, 1000 * abs(hi - lo)))
    #   xdiff = (pa[0] - ea[0], pb[0] - eb[0])
    #   ydiff = (pa[1] - ea[1], pb[1] - eb[1])

    #   div = det(xdiff, ydiff)
    #   if div == 0:
    #     continue

    #   d = (det(pa, ea), det(pb, eb))
    #   x = det(d, xdiff) / div
    #   y = det(d, ydiff) / div

    #   # if (a in crashed and crashed[a] ) or b in crashed:
    #   #   print(a, b, 'already crashed', div)
    #   #   continue

    #   if lo <= x <= hi and lo <= y <= hi:
    #     # if not (inside(x, (pa[0], ea[0])) and inside(x, (pb[0], eb[0]))):
    #     if not (same_dir(x, pa, va) and same_dir(x, pb, vb)):
    #       print(x, 'outside', (pa[0], ea[0]), (pb[0], eb[0]))
    #       continue
    #     print(a,b, 'intersected at', (x,y), div)
    #     # crashed.add(a)
    #     # crashed.add(b)
    #     total += 1

    return total

if __name__ == '__main__':
  # part1_sample = main(readFileName('s.txt'), 1, 7, 27)
  # print('Part 1 (sample):', part1_sample)
  # assert part1_sample == 2

  # part1_real = main(readFileName('r.txt'), 1, 200000000000000, 400000000000000)
  # print('Part 1 (real):', part1_real)
  # assert part1_real == 0

  part2_sample = main(readFileName('s.txt'), 2, 0, 0)
  print('Part 2 (sample):', part2_sample)
  assert part2_sample == 0

  part2_real = main(readFileName('r.txt'), 2, 0, 0)
  print('Part 2 (real):', part2_real)
  # assert part2_real == 0
