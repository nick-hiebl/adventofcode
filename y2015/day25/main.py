from utils import *

def get_nth(index):
  val = 20151125

  while index > 1:
    val *= 252533
    val %= 33554393

    index -= 1

  return val

def strip_length(row, col):
  return row + col - 1

def to_index(row, col):
  r = 1
  c = 1

  index = 1

  while r < row:
    index += strip_length(r, c)
    r += 1
  
  while c < col:
    index += strip_length(r, c) + 1
    c += 1

  return index

def main(row, col, part = 1):
  
  index = to_index(row, col)

  if part == 1:
    return get_nth(index)
  else:
    return get_nth(index)

if __name__ == '__main__':
  part1_sample = main(4, 2)
  print('Part 1 (sample):', part1_sample)
  assert part1_sample == 32451966

  part1_real = main(2947, 3029)
  print('Part 1 (real):', part1_real)
  assert part1_real == 10723906903

  part2_sample = main(4, 2, 2)
  print('Part 2 (sample):', part2_sample)
  assert part2_sample == 44

  part2_real = main(2947, 3029, 2)
  print('Part 2 (real):', part2_real)
  # assert part2_real == 0
