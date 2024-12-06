from utils import *
import re

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def next_dir(drn):
  return DIRS[(DIRS.index(drn) + 1) % len(DIRS)]

def processInput(data):
  out = []
  pos = tuple()

  for r,line in enumerate(data):
    if '^' in line:
      out.append(line.replace('^', '.'))
      pos = (r, line.index('^'))
    else:
      out.append(line)

  return pos, out

def step(room, pos, drn):
  after = tadd(pos, drn)
  r,c = after
  if not (0 <= r < len(room) and 0 <= c < len(room[0])):
    return pos, drn
  
  if room[r][c] == '#':
    return pos, next_dir(drn)
  return after, drn

def walk_loops(room, start):
  pos, drn = start, DIRS[0]

  seen = set()

  while True:
    state = (pos, drn)
    if state in seen:
      return True

    seen.add(state)
    
    after = step(room, pos, drn)
    if after == (pos, drn):
      return False
    pos,drn = after

def main(raw, part):
  pos, room = processInput(raw)

  starter = pos
  drn = DIRS[0]
  
  visited = set()

  while True:
    visited.add(pos)

    future = step(room, pos, drn)

    if future == (pos, drn):
      break
    pos, drn = future

  if part == 1:
    return len(visited)

  assert walk_loops(room, starter) == False

  obstacles = 0
  for v in visited:
    if visited == starter:
      continue

    plan = room[:]
    r,c = v
    row = list(plan[r])
    row[c] = '#'
    plan[r] = ''.join(row)

    if walk_loops(plan, starter):
      # print(v)
      obstacles += 1

  return obstacles

if __name__ == '__main__':
  part1_sample = main(readFileName('s.txt'), 1)
  print('Part 1 (sample):', part1_sample)
  assert part1_sample == 41

  part1_real = main(readFileName('r.txt'), 1)
  print('Part 1 (real):', part1_real)
  assert part1_real == 4647

  part2_sample = main(readFileName('s.txt'), 2)
  print('Part 2 (sample):', part2_sample)
  assert part2_sample == 6

  part2_real = main(readFileName('r.txt'), 2)
  print('Part 2 (real):', part2_real)
  assert part2_real == 1723
