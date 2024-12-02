from utils import *
import re

def processInput(data):
  return data

def main(raw, part):
  res = ''

  data = processInput(raw)

  if part == 1:
    cols = zip(*data)
    # print(list(counts_of_iterable(col) for col in cols))
    for col in cols:
      cs = counts_of_iterable(col)
      res += sorted(cs.items(), key=lambda x: -x[1])[0][0]
    return res
  elif part == 2:
    cols = zip(*data)
    # print(list(counts_of_iterable(col) for col in cols))
    for col in cols:
      cs = counts_of_iterable(col)
      res += sorted(cs.items(), key=lambda x: x[1])[0][0]
    return res

if __name__ == '__main__':
  part1_sample = main(readFileName('s.txt'), 1)
  print('Part 1 (sample):', part1_sample)
  assert part1_sample == 'easter'

  part1_real = main(readFileName('r.txt'), 1)
  print('Part 1 (real):', part1_real)
  assert part1_real == 'afwlyyyq'

  part2_sample = main(readFileName('s.txt'), 2)
  print('Part 2 (sample):', part2_sample)
  assert part2_sample == 'advent'

  part2_real = main(readFileName('r.txt'), 2)
  print('Part 2 (real):', part2_real)
  # assert part2_real == 0
