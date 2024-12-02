from utils import *
import re
from sympy import symbols, solve
from itertools import combinations

def processInput(data):
  out = []

  for line in data:
    out.append(tuple(map(int, line.replace(' @', ',').split(', '))))
    # a,b = tuple(map(int, x.split(', '))), tuple(map(int, y.split(', ')))

    # out.append((a,b))

  return out

def intersects(stone1, stone2):
  x, y, t1, t2 = symbols('x y t1 t2')

  equations = []
  for (ax, ay, _, dx, dy, _), t in zip([stone1, stone2], [t1, t2]):
    equations += [
      ax + dx * t - x,
      ay + dy * t - y
    ]

  soln = solve(equations)
  # print('>>>>>>', stone1, stone2)
  if not soln:
    return None
  # print(type(soln), soln)
  if soln[t1] >= 0 and soln[t2] >= 0:
    # print('WORKS')
    return (soln[x], soln[y])
  return None

def main(raw, part, lo = 7, hi = 27):
  total = 0

  hailstones = processInput(raw)

  if part == 1:
    total = 0
    nos = len(list(combinations(hailstones, 2)))
    print(nos)
    for i, (a, b) in enumerate(combinations(hailstones, 2)):
      p = intersects(a, b)
      if i % 100 == 0:
        print(i, '/', nos)
      if not p:
        continue
      x,y = p
      if lo <= x <= hi and lo <= y <= hi:
        total += 1

    return total
  elif part == 2:
    rx, ry, rz, rdx, rdy, rdz, t1, t2, t3 = symbols('rx ry rz rdx rdy rdz t1 t2 t3')
    equations = []
    for (x,y,z,dx,dy,dz),t in zip(hailstones, [t1,t2,t3]):
      equations += [
        rx + t * rdx - (x + t * dx),
        ry + t * rdy - (y + t * dy),
        rz + t * rdz - (z + t * dz)
      ]

    soln = solve(equations)
    print(soln)
    print(soln[0])
    v = (soln[0][rx] + soln[0][ry] + soln[0][rz])

    return v

if __name__ == '__main__':
  part1_sample = main(readFileName('s.txt'), 1)
  print('Part 1 (sample):', part1_sample)
  assert part1_sample == 2

  part1_real = main(readFileName('r.txt'), 1, 200000000000000, 400000000000000)
  print('Part 1 (real):', part1_real)
  assert part1_real == 24192

  part2_sample = main(readFileName('s.txt'), 2)
  print('Part 2 (sample):', part2_sample)
  assert part2_sample == 47

  part2_real = main(readFileName('r.txt'), 2)
  print('Part 2 (real):', part2_real)
  # assert part2_real == 0
