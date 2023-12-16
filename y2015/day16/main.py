from utils import *
import re

def processInput(data):
  out = []
  for i_, line in enumerate(data):
    i = i_+1
    suename, d = re.split(' [0-9]+: ', line)
    x = {}
    for d2 in d.split(', '):
      f, v = d2.split(': ')
      x[f] = int(v)
    out.append((i, x))
  return out

CHECK = {
  "children": 3,
  "cats": 7,
  "samoyeds": 2,
  "pomeranians": 3,
  "akitas": 0,
  "vizslas": 0,
  "goldfish": 5,
  "trees": 3,
  "cars": 2,
  "perfumes": 1
}

def main(raw, part):
  total = 0

  data = processInput(raw)

  if part == 1:  
    for num, attrs in data:
      if all(attrs[k] == CHECK[k] for k in attrs.keys()):
        return num
  elif part == 2:
    for num, attrs in data:
      if all(attrs[k] > CHECK[k] if k in ('cats', 'trees') else attrs[k] < CHECK[k] if k in ('pomeranians', 'goldfish') else attrs[k] == CHECK[k] for k in attrs.keys()):
        return num

if __name__ == '__main__':
  # part1_sample = main(readFileName('s.txt'), 1)
  # print('Part 1 (sample):', part1_sample)
  # assert part1_sample == None

  part1_real = main(readFileName('r.txt'), 1)
  print('Part 1 (real):', part1_real)
  assert part1_real == 373

  # part2_sample = main(readFileName('s.txt'), 2)
  # print('Part 2 (sample):', part2_sample)
  # assert part2_sample == None

  part2_real = main(readFileName('r.txt'), 2)
  print('Part 2 (real):', part2_real)
  # assert part2_real == None
