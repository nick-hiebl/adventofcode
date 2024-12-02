from utils import *
import re
from collections import *
from queue import PriorityQueue

def processInput(data):
  out = []

  for i,line in enumerate(data):
    b1,b2 = line.split('~')
    key = i
    # key = chr(ord('A') + i)
    out.append((key, tuple(map(int,b1.split(','))), tuple(map(int,b2.split(',')))))

  return out


def falling_if_removed(above, below, top, x):
  removed = {x}

  removed_from = defaultdict(set)
  removed_from[top[x]].add(x)

  t = 0
  queue = PriorityQueue()

  queue.put(top[x])

  evaluated = set()
  added = set()

  while not queue.empty():
    h = queue.get()

    if h in evaluated:
      continue
    evaluated.add(h)

    for brick in removed_from[h]:
      for over in above[brick]:
        if all(x in removed for x in below[over]):
          removed.add(over)
          if top[over] not in added:
            queue.put(top[over])
            added.add(top[over])
          removed_from[top[over]].add(over)

  return len(removed) - 1

def main(raw, part):
  total = 0

  data = processInput(raw)

  bricks = []

  # print('No. of bricks', len(data))

  highest_at = {}
  resting_on = {}
  tiptop = {}

  maxlen = 0
  data.sort(key=lambda x: min(x[1][2], x[2][2]))
  for i,e1,e2 in data:
    bottom = min(e1[2],e2[2])
    size = sum(abs(a-b) for a,b in zip(e1,e2)) + 1
    xs,ys,zs = (sorted([e1[i], e2[i]]) for i in range(3))

    lowest_free,unders = 1,set()
    for x in range(xs[0], xs[1] + 1):
      for y in range(ys[0], ys[1] + 1):
        if (x,y) not in highest_at:
          continue
        brick,height = highest_at[(x,y)]
        # lowest_free = max(lowest_free, height + 1)
        if height > lowest_free:
          lowest_free = height
          unders = set()
          unders.add(brick)
        elif height == lowest_free:
          unders.add(brick)
        else:
          # Too low, who cares
          pass
    
    resting_on[i] = unders
    # print(highest_at)

    # print((e1, e2))

    # print('Brick', i, 'settling upon', unders)

    # print('Hopefully', bottom, lowest_free)
    assert bottom >= lowest_free

    drop_by = bottom - lowest_free
    z = max(zs) - drop_by
    tiptop[i] = z
    for x in range(xs[0], xs[1] + 1):
      for y in range(ys[0], ys[1] + 1):
        # print('Settling brick to', z)
        if (x,y) not in highest_at:
          highest_at[(x,y)] = (i, z + 1)
        else:
          other,their_h = highest_at[(x,y)]

          assert their_h <= min(zs) - drop_by
          # Mark brick
          highest_at[(x,y)] = (i, z + 1)

  overs = defaultdict(set)

  for brick in resting_on.keys():
    for under in resting_on[brick]:
      overs[under].add(brick)

  if part == 1:
    total = 0
    for brick,_,__ in data:
      if all(resting_on[x] != {brick} for x in overs[brick]):
        total += 1

    return total
  elif part == 2:
    total = 0
    for brick,_,__ in data:
      c = falling_if_removed(overs, resting_on, tiptop, brick)
      total += c
    return total

if __name__ == '__main__':
  part1_sample = main(readFileName('s.txt'), 1)
  print('Part 1 (sample):', part1_sample)
  assert part1_sample == 5

  part1_real = main(readFileName('r.txt'), 1)
  print('Part 1 (real):', part1_real)
  assert part1_real == 443

  part2_sample = main(readFileName('s.txt'), 2)
  print('Part 2 (sample):', part2_sample)
  assert part2_sample == 7

  part2_real = main(readFileName('r.txt'), 2)
  print('Part 2 (real):', part2_real)
  assert part2_real == 69915
