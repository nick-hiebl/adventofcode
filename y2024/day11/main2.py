from utils import *

def processInput(data):
  return tuple(map(int, data[0].split()))

def split_stone(stone):
  l = len(str(stone))
  return int(str(stone)[:l//2]), int(str(stone)[l//2:])

def blink(stones, depth):
  counts = {}
  for stone in stones:
    counts[stone] = counts.get(stone, 0) + 1

  for i in range(depth):
    after = {}
    for stone, count in counts.items():
      if stone == 0:
        after[1] = after.get(1, 0) + count
      elif len(str(stone)) % 2 == 0:
        left,right = split_stone(stone)
        after[left] = after.get(left, 0) + count
        after[right] = after.get(right, 0) + count
      else:
        after[stone * 2024] = after.get(stone * 2024, 0) + count
    counts = after
  # print(counts)
  print(len(counts.keys()))
  return sum(counts.values())

def main(raw, part):
  data = processInput(raw)

  if part == 1:
    stones = data
    return blink(stones, 25)
  elif part == 2:
    stones = data
    return blink(stones, 75)
  elif part == 3:
    stones = data
    return blink(stones, 9999)

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
