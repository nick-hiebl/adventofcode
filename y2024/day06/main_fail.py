from utils import *
import re

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def processInput(data):
  out = []
  pos = (0, 0)

  for r, line in enumerate(data):
    if '^' in line:
      pos = (r, line.index('^'))
      out.append(line.replace('^', '.'))
    else:
      out.append(line)

  return out, pos

def posses(seen):
  return set(pos for pos,_ in seen)

def next_dir(drn):
  return DIRS[(DIRS.index(drn) + 1) % len(DIRS)]

def step(plan, pos, drn):
  after = tadd(pos, drn)
  try:
    if plan[after[0]][after[1]] == '#':
      return pos, next_dir(drn)
    else:
      return after, drn
  except:
    return pos, drn

def walk_loops(plan, pos, drn):
  seen = set()
  while True:
    state = (pos,drn)
    if state in seen:
      return True
    seen.add(state)
    future = step(plan, pos, drn)
    if future == state:
      return False
    pos, drn = future

def replace_i(st, ind, val):
  return st[:ind] + val + st[ind+1:]

def main(raw, part):
  total = 0

  plan, pos = processInput(raw)
  starter = pos

  print('\n'.join(plan))

  if part == 3:
    drn = DIRS[0]
    seen = set()
    path = set()

    while True:
      state = (pos, drn)
      path.add(pos)
      if state in seen:
        break
      seen.add(state)
      after = tadd(pos, drn)

      future = step(plan, pos, drn)
      if future == state:
        break
      pos, drn = future

    jjj = 0
    for q, spot in enumerate(path):
      if spot == starter:
        continue
      if q % 100 == 0:
        print(q, '/', len(path))

      r,c = spot
      plan2 = plan[:]
      base = plan2[r]
      assert base[c] == '.'
      plan2[r] = replace_i(base, c, '#')

      if walk_loops(plan2, starter, DIRS[0]):
        jjj += 1
      # plan[r] = base
    return jjj


  if part == 1:
    drn = DIRS[0]
    seen = set()
    path = 0

    while True:
      path += 1
      state = (pos, drn)
      if state in seen:
        return len(posses(seen))
      seen.add(state)
      after = tadd(pos, drn)

      future = step(plan, pos, drn)
      if future == state:
        return len(posses(seen))
      pos, drn = future

  elif part == 2:
    drn = DIRS[0]
    seen = set()
    specials = set()
    jk = 0

    while True:
      jk += 1
      if jk % 100 == 0:
        print(jk)
      state = (pos, drn)
      if state in seen:
        break
      seen.add(state)
      after = tadd(pos, drn)
      try:
        if plan[after[0]][after[1]] == '#':
          drn = next_dir(drn)
        else:
          if not after in specials:
            current = plan[after[0]]
            with_t = replace_i(current, after[1], '#')
            plan[after[0]] = with_t

            if walk_loops(plan, pos, drn):
              specials.add(after)

            plan[after[0]] = current

          pos = after
      except:
        break

    print(specials)
    if starter in specials:
      print('Starter was in specials. Removing them.')
      specials.remove(starter)
    return len(specials)



if __name__ == '__main__':
  # part1_sample = main(readFileName('s.txt'), 1)
  # print('Part 1 (sample):', part1_sample)
  # assert part1_sample == 41

  part1_real = main(readFileName('r.txt'), 1)
  print('Part 1 (real):', part1_real)
  assert part1_real == 4647

  part2_sample = main(readFileName('s.txt'), 3)
  print('Part 2 (sample):', part2_sample)
  assert part2_sample == 6

  # part2_real = main(readFileName('r.txt'), 2)
  # print('Part 2 (real):', part2_real)
  # # assert part2_real == 0
  part2_real = main(readFileName('r.txt'), 3)
  print('Part 3 (real):', part2_real)
  # assert part2_real == 0
