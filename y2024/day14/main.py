from utils import *
import re
import time

def processInput(data):
  out = []

  for line in data:
    p,v = [x.split('=')[1] for x in line.split(' ')]
    pd = tuple(map(int, p.split(',')))
    vd = tuple(map(int, v.split(',')))

    out.append((pd, vd))

  # print(out)
  return out

def simulate_steps(robots, dimns, steps):
  quarters = [0, 0, 0, 0]
  cGrid = [[0 for j in range(dimns[0])] for i in range(dimns[1])]
  for p, v in robots:
    v2 = tuple(x % y for x, y in zip(tadd(dimns, v), dimns))
    total_move = tuple(vd * steps for vd in v2)
    final_rel = tuple(x % y for x,y in zip(total_move, dimns))
    final_pos = tadd(p, final_rel)
    centered = tuple(x % y for x,y in zip(final_pos, dimns))
    x,y = centered
    cGrid[y][x] += 1
    if x < dimns[0] // 2:
      if y < dimns[1] // 2:
        quarters[0] += 1
      elif y > dimns[1] // 2:
        quarters[1] += 1
    elif x > dimns[0] // 2:
      if y < dimns[1] // 2:
        quarters[2] += 1
      elif y > dimns[1] // 2:
        quarters[3] += 1

  for row in cGrid:
    print(''.join(str(n) if n > 0 else '.' for n in row))
    
  val = quarters[0] * quarters[1] * quarters[2] * quarters[3]
  print(val, quarters)
  return val

def main(raw, part, real):
  dimns = (101, 103) if real else (11, 7)
  total = 0

  data = processInput(raw)

  if part == 1:
    return simulate_steps(data, dimns, 100)
  elif part == 2:
    i = 0
    while True:
      s = ['vert' if ((i - 317) % 101) == 0 else '', 'hori' if ((i - 300) % 103 == 0) else '']
      if 'hori' in s or 'vert' in s:
        print(i, s)
        simulate_steps(data, dimns, i)
        if (s.count('') == 0):
          input()
      i += 1
    return total

if __name__ == '__main__':
  part1_sample = main(readFileName('s.txt'), 1, False)
  print('Part 1 (sample):', part1_sample)
  assert part1_sample == 12

  part1_real = main(readFileName('r.txt'), 1, True)
  print('Part 1 (real):', part1_real)
  assert part1_real == 225943500

  # part2_sample = main(readFileName('s.txt'), 2, False)
  # print('Part 2 (sample):', part2_sample)
  # assert part2_sample == 0

  part2_real = main(readFileName('r.txt'), 2, True)
  print('Part 2 (real):', part2_real)
  # assert part2_real == 0

# Vert stripe: 317, 418, 519, 618, 717, 816, 915, 1014
# Horiz stripe: 300, 403, 506, 609, 712, 815