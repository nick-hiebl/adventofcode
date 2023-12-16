from utils import *
import json

def processInput(data):
  return json.loads('\n'.join(data))

def walkAndSum(data, part=1):
  t = 0

  if type(data) == type(0):
    return data
  if type(data) == type({}):
    if part == 2 and "red" in data.values():
      return 0
    # print('part', part)
    for k in data.values():
      t += walkAndSum(k, part)
    return t
  if type(data) == type([]):
    return sum(walkAndSum(x, part) for x in data)
  return 0

def main(raw, part):
  total = 0

  data = processInput(raw)

  # print(part, 'part')
  if part == 1:  
    return walkAndSum(data, part)
  elif part == 2:
    return walkAndSum(data, part)

if __name__ == '__main__':
  part1_sample = main(readFileName('s.txt'), 1)
  print('Part 1 (sample):', part1_sample)
  assert part1_sample == 0

  part1_real = main(readFileName('r.txt'), 1)
  print('Part 1 (real):', part1_real)
  assert part1_real == 111754

  part2_sample = main(readFileName('s.txt'), 2)
  print('Part 2 (sample):', part2_sample)
  assert part2_sample == 0

  part2_real = main(readFileName('r.txt'), 2)
  print('Part 2 (real):', part2_real)
  # assert part2_real == 0
