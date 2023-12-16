from utils import *
import re
import itertools
import functools

def processInput(data):
  out = []
  for line in data:
    l = tuple([int(x.split(' ')[1]) for x in line.split(': ')[1].split(', ')])
    out.append(l)
  return out

def main(raw, part):
  total = 0

  data = processInput(raw)
  print(data)

  if part == 1:
    best = 0
    for comb in itertools.combinations_with_replacement(data, 100):
      scores = functools.reduce(tadd, comb)
      a,b,c,d,cal = scores
      if a < 0 or b < 0 or c < 0 or d < 0:
        continue
      best = max(best, a * b * c * d)
    return best
  elif part == 2:
    best = 0
    for comb in itertools.combinations_with_replacement(data, 100):
      scores = functools.reduce(tadd, comb)
      a,b,c,d,cal = scores
      if a < 0 or b < 0 or c < 0 or d < 0 or cal != 500:
        continue
      best = max(best, a * b * c * d)
    return best

if __name__ == '__main__':
  # Slooooow one, all up takes 36s on my machine
  part1_sample = main(readFileName('s.txt'), 1)
  print('Part 1 (sample):', part1_sample)
  assert part1_sample == 62842880

  part1_real = main(readFileName('r.txt'), 1)
  print('Part 1 (real):', part1_real)
  assert part1_real == 21367368

  part2_sample = main(readFileName('s.txt'), 2)
  print('Part 2 (sample):', part2_sample)
  assert part2_sample == 57600000

  part2_real = main(readFileName('r.txt'), 2)
  print('Part 2 (real):', part2_real)
  # assert part2_real == 1766400
