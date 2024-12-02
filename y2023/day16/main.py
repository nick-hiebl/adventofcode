from utils import *
import re
import sys

# sys.setrecursionlimit(100000)

def processInput(data):
  out = []

  for line in data:
    out.append(line)

  return out

RIGHT = (0, 1)
LEFT = (0, -1)
UP = (-1, 0)
DOWN = (1, 0)

def traverse(pos, drn, grid, energies, seen):
  while True:
    pos = tadd(pos, drn)
    r,c = pos
    if (pos, drn) in seen:
      return
    if r < 0 or r >= len(grid):
      return
    if c < 0 or c >= len(grid[r]):
      return
    energies[r][c] = 1
    seen[(pos, drn)] = True
    
    cell = grid[r][c]
    if cell == '/':
      if drn == UP:
        return traverse(pos, RIGHT, grid, energies, seen)
      elif drn == DOWN:
        return traverse(pos, LEFT, grid, energies, seen)
      elif drn == RIGHT:
        return traverse(pos, UP, grid, energies, seen)
      elif drn == LEFT:
        return traverse(pos, DOWN, grid, energies, seen)
    elif cell == '\\':
      if drn == UP:
        return traverse(pos, LEFT, grid, energies, seen)
      elif drn == DOWN:
        return traverse(pos, RIGHT, grid, energies, seen)
      elif drn == RIGHT:
        return traverse(pos, DOWN, grid, energies, seen)
      elif drn == LEFT:
        return traverse(pos, UP, grid, energies, seen)
    elif cell == '|':
      if drn == LEFT or drn == RIGHT:
        traverse(pos, UP, grid, energies, seen)
        traverse(pos, DOWN, grid, energies, seen)
        return
    elif cell == '-':
      if drn == UP or drn == DOWN:
        traverse(pos, LEFT, grid, energies, seen)
        traverse(pos, RIGHT, grid, energies, seen)
        return

def checkForMe(start, drn, data):
  energy = [[0] * len(row) for row in data]
  seen = {}
  traverse(start, drn, data, energy, {})
  return sum(map(sum, energy))

def main(raw, part):
  total = 0

  data = processInput(raw)

  if part == 1:
    return checkForMe((0, -1), RIGHT, data)
  elif part == 2:
    b = 0
    w = len(data[0])
    h = len(data)
    for c in range(w):
      b = max(b, checkForMe((-1, c), DOWN, data))
      b = max(b, checkForMe((h, c), UP, data))
    for r in range(h):
      b = max(b, checkForMe((r, -1), RIGHT, data))
      b = max(b, checkForMe((r, w), LEFT, data))
    return b

if __name__ == '__main__':
  part1_sample = main(readFileName('s.txt'), 1)
  print('Part 1 (sample):', part1_sample)
  assert part1_sample == 46

  part1_real = main(readFileName('r.txt'), 1)
  print('Part 1 (real):', part1_real)
  assert part1_real == 7939

  part2_sample = main(readFileName('s.txt'), 2)
  print('Part 2 (sample):', part2_sample)
  # assert part2_sample == 0

  part2_real = main(readFileName('r.txt'), 2)
  print('Part 2 (real):', part2_real)
  # assert part2_real == 0
