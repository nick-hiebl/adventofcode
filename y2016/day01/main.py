from utils import *

def processInput(data):
  out = []

  for line in data[0].split(', '):
    out.append((line[0], int(line[1:])))

  return out

def main(raw, part):
  drn = (0, 1)
  pos = (0, 0)

  data = processInput(raw)

  if part == 1:
    for rot, steps in data:
      if rot == 'R':
        x,y = drn
        drn = (y, -x)
      else:
        x,y = drn
        drn = (-y, x)
      pos = tadd(pos, ttimes(drn, steps))
    return sum(pos)
  elif part == 2:
    seen = set()
    seen.add(pos)
    for rot, steps in data:
      if rot == 'R':
        x,y = drn
        drn = (y, -x)
      else:
        x,y = drn
        drn = (-y, x)
      for _ in range(steps):
        pos = tadd(pos, drn)
        if pos in seen:
          print(pos)
          return sum(map(abs, pos))
        seen.add(pos)
        
    raise Exception()

if __name__ == '__main__':
  part1_sample = main(readFileName('s.txt'), 1)
  print('Part 1 (sample):', part1_sample)
  assert part1_sample == 12

  part1_real = main(readFileName('r.txt'), 1)
  print('Part 1 (real):', part1_real)
  assert part1_real == 271

  part2_sample = main(readFileName('s2.txt'), 2)
  print('Part 2 (sample):', part2_sample)
  assert part2_sample == 4

  part2_real = main(readFileName('r.txt'), 2)
  print('Part 2 (real):', part2_real)
  # assert part2_real == 0
