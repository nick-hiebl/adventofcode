from utils import *
import re

def processInput(data):
  return [int(x) for x in data]

def iterateCombs(buckets, eggnog, space, soln):
  # print('Trying:', buckets, eggnog, space, soln)
  if eggnog < 0 or space == 0:
    return 0
  if eggnog == 0:
    return 1
  if space == eggnog:
    return 1
  if eggnog > space:
    return 0
  me = buckets[0]
  return iterateCombs(buckets[1:], eggnog - me, space - me, soln + [me]) \
    + iterateCombs(buckets[1:], eggnog, space - me, soln)

def yieldCombs(buckets, eggnog, space, soln):
  # print('Trying:', buckets, eggnog, space, soln)
  if eggnog < 0 or (space == 0 and eggnog > 0):
    pass
  elif eggnog == 0:
    yield soln
  elif space == eggnog:
    yield soln + buckets
  elif eggnog > space:
    pass
  else:
    me = buckets[0]
    for x in yieldCombs(buckets[1:], eggnog - me, space - me, soln + [me]):
      yield x
    for x in yieldCombs(buckets[1:], eggnog, space - me, soln):
      yield x

def main(raw, part):
  total = 0

  data = processInput(raw)

  if part == 1:  
    return iterateCombs(data, 150, sum(data), [])
  elif part == 2:
    fewest = 1000
    ways = 0
    for comb in yieldCombs(data, 150, sum(data), []):
      if len(comb) < fewest:
        fewest = len(comb)
        ways = 1
      elif len(comb) == fewest:
        ways += 1
    print(fewest, ways)
    return ways

if __name__ == '__main__':
  part1_sample = main(readFileName('s.txt'), 1)
  print('Part 1 (sample):', part1_sample)
  assert part1_sample == 0

  part1_real = main(readFileName('r.txt'), 1)
  print('Part 1 (real):', part1_real)
  assert part1_real == 4372

  part2_sample = main(readFileName('s.txt'), 2)
  print('Part 2 (sample):', part2_sample)
  assert part2_sample == 0

  part2_real = main(readFileName('r.txt'), 2)
  print('Part 2 (real):', part2_real)
  # assert part2_real == 0
