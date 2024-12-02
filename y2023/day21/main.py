from utils import *
import re

def processInput(data):
  out = []

  for line in data:
    out.append(line)

  return out

def main(raw, part, n):
  total = 0

  data = processInput(raw)

  start = (0,0)
  for v,rc,row in enumerateGrid(data):
    if v == 'S':
      start = rc
      break

  if part == 1:
    g = grid_to_graph(data, lambda f,t: data[t[0]][t[1]] != '#', False)

    return flood_in_exactly(g, start, n)
  elif part == 2:
    g = wrapping_grid_to_graph(data, lambda x,y: y != '#', False)

    return flood_in_exactly2(g, start, n, data)

if __name__ == '__main__':
  part1_sample = main(readFileName('s.txt'), 1, 6)
  print('Part 1 (sample):', part1_sample)
  assert part1_sample == 16

  part1_real = main(readFileName('r.txt'), 1, 64)
  print('Part 1 (real):', part1_real)
  assert part1_real == 3716

  part2_sample = main(readFileName('s.txt'), 2, 6)[-1]
  print('Part 2 (sample):', part2_sample)
  assert part2_sample == 16

  part2_sample = main(readFileName('s.txt'), 2, 10)[-1]
  print('Part 2 (sample):', part2_sample)
  assert part2_sample == 50

  part2_sample = main(readFileName('s.txt'), 2, 100)[-1]
  print('Part 2 (sample):', part2_sample)
  assert part2_sample == 6536

  # part2_sample = main(readFileName('s.txt'), 2, 500)
  # print('Part 2 (sample):', part2_sample)
  # assert part2_sample == 167004

  part2_real = main(readFileName('r.txt'), 2, 65)
  print('Part 2 65 (real):', part2_real)

  # part2_real = main(readFileName('r.txt'), 2, 130)
  # print('Part 2 130 (real):', part2_real)

  part2_real = main(readFileName('r.txt'), 2, 600)
  print('Part 2 327 (real):', part2_real)
  # assert part2_real == 0
