from utils import *
import re

def processInput(data):
  out = []

  for line in data:
    results = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', line)
    print(results)
    out += results

  return out

def processInput2(data):
  out = []

  for line in data:
    results = re.findall(r'(mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\))', line)
    print(results)
    out += results

  return out

def process(cmd):
  nums = [int(x) for x in re.findall(r'[0-9]+', cmd)]
  c = 1
  for n in nums:
    c *= n
  return c

def main(raw, part):
  total = 0


  if part == 1:
    data = processInput(raw)
    for cmd in data:
      total += process(cmd)
      # nums = [int(x) for x in re.findall(r'[0-9]+', cmd)]
      # c = 1
      # for n in nums:
      #   c *= n
      # total += c
    return total
  elif part == 2:
    data = processInput2(raw)
    en = True
    for cmd in data:
      if cmd == 'do()':
        en = True
        continue
      elif cmd == 'don\'t()':
        en = False
        continue

      if en:
        total += process(cmd)
    return total

if __name__ == '__main__':
  part1_sample = main(readFileName('s.txt'), 1)
  print('Part 1 (sample):', part1_sample)
  assert part1_sample == 161

  part1_real = main(readFileName('r.txt'), 1)
  print('Part 1 (real):', part1_real)
  assert part1_real == 184511516

  part2_sample = main(readFileName('s2.txt'), 2)
  print('Part 2 (sample):', part2_sample)
  assert part2_sample == 48

  part2_real = main(readFileName('r.txt'), 2)
  print('Part 2 (real):', part2_real)
  # assert part2_real == 0
