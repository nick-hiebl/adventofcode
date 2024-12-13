from utils import *
import re
from queue import PriorityQueue
import math
import numpy as np
from sympy import symbols, solve

def processInput(data):
  out = []

  current = {}
  # out.append(current)

  for line in data:    
    if line.startswith('Button A:'):
      current = {}
      out.append(current)
      _, ts = line.split(': ')
      xs, ys = ts.split(', ')
      xo, yo = xs.split('+')[1], ys.split('+')[1]
      current['A'] = (int(xo), int(yo))
    if line.startswith('Button B:'):
      _, ts = line.split(': ')
      xs, ys = ts.split(', ')
      xo, yo = xs.split('+')[1], ys.split('+')[1]
      current['B'] = (int(xo), int(yo))
    if line.startswith('Prize:'):
      _, ts = line.split(': ')
      xs, ys = ts.split(', ')
      xo, yo = xs.split('=')[1], ys.split('=')[1]
      current['Prize'] = (int(xo), int(yo))

  return out

def solve_machine(machine):
  a = machine['A']
  b = machine['B']
  target = machine['Prize']

  q = PriorityQueue()

  q.put((0, 0, (0, 0)))

  seen = set()

  xl = math.gcd(a[0], b[0])
  yl = math.gcd(a[1], b[1])
  if target[0] % xl != 0 or target[1] % yl != 0:
    return -1

  while not q.empty():
    w, ps, current = q.get()
    if current in seen:
      continue
    seen.add(current)
    # print('Considering', current)
    if current == target:
      return w
    if current[0] >= target[0] or current[1] >= target[1]:
      continue
    if ps >= 200:
      continue

    q.put((w+3, ps+1, tadd(current, a)))
    q.put((w+1, ps+1, tadd(current, b)))

  return -1

def solve1(machine):
  a = machine['A']
  b = machine['B']
  target = machine['Prize']

  aps, bps = symbols('aps bps')

  equations = []
  equations += [a[0] * aps + b[0] * bps - target[0]]
  equations += [a[1] * aps + b[1] * bps - target[1]]
  soln = solve(equations)

  # print(soln)
  if not soln:
    return 0
  ax = soln[aps]
  bx = soln[bps]

  if ax != int(ax) or bx != int(bx):
    return 0
  if ax > 100 or bx > 100:
    return 0
  return ax * 3 + bx

def solve2(machine):
  a = machine['A']
  b = machine['B']
  target = tadd(machine['Prize'], (10000000000000, 10000000000000))

  aps, bps = symbols('aps bps')

  equations = []
  equations += [a[0] * aps + b[0] * bps - target[0]]
  equations += [a[1] * aps + b[1] * bps - target[1]]
  soln = solve(equations)

  # print(soln)
  if not soln:
    return 0
  ax = soln[aps]
  bx = soln[bps]
  if ax != int(ax) or bx != int(bx):
    return 0
  return ax * 3 + bx

def main(raw, part):
  total = 0

  data = processInput(raw)
  # print(data)

  if part == 1:
    for machine in data:
      cost = solve1(machine)

      if cost > 0:
        total += cost
    return total
  elif part == 2:
    for machine in data:
      total += solve2(machine)

    return total

if __name__ == '__main__':
  part1_sample = main(readFileName('s.txt'), 1)
  print('Part 1 (sample):', part1_sample)
  assert part1_sample == 480

  part1_real = main(readFileName('r.txt'), 1)
  print('Part 1 (real):', part1_real)
  assert part1_real == 26299

  part2_sample = main(readFileName('s.txt'), 2)
  print('Part 2 (sample):', part2_sample)
  # assert part2_sample == 1

  part2_real = main(readFileName('r.txt'), 2)
  print('Part 2 (real):', part2_real)
  # assert part2_real == 0
