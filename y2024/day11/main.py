from utils import *
import sys
from functools import cache

sys.setrecursionlimit(12000)

def processInput(data):
  return tuple(map(int, data[0].split()))

@cache
def blink(stone, n):
  if n == 0:
    return 1
  total = 0
  if stone == 0:
    total += blink(1, n-1)
  elif len(str(stone)) % 2 == 0:
    l = len(str(stone))
    total += blink(int(str(stone)[:l//2]), n-1)
    total += blink(int(str(stone)[l//2:]), n-1)
  else:
    total += blink(stone * 2024, n-1)
  return total

def blinkall(stones, n):
  return sum(blink(stone, n) for stone in stones)

def main(raw, part):
  data = processInput(raw)

  if part == 1:
    stones = data
    return blinkall(stones, 25)
  elif part == 2:
    stones = data
    return blinkall(stones, 75)
  elif part == 3:
    stones = data
    return blinkall(stones, 1000)

if __name__ == '__main__':
  part1_sample = main(readFileName('s.txt'), 1)
  print('Part 1 (sample):', part1_sample)
  assert part1_sample == 55312

  part1_real = main(readFileName('r.txt'), 1)
  print('Part 1 (real):', part1_real)
  assert part1_real == 217812

  # part2_sample = main(readFileName('s.txt'), 2)
  # print('Part 2 (sample):', part2_sample)
  # assert part2_sample == 0

  part2_real = main(readFileName('r.txt'), 2)
  print('Part 2 (real):', part2_real)
  # assert part2_real == 0

  part3_real = main(readFileName('r.txt'), 3)
  print('Part 3 (real):', part3_real)
