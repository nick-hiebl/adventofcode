from utils import *
import re

def processInput(data):
  return data

def supports_snoop(s):
  abbas = list(filter(lambda x: x[0] != x[1], re.findall(r'([a-z])([a-z])\2\1', s)))
  groups = counts_of_iterable(abbas)
  inners = counts_of_iterable(re.findall(r'\[[^\[\]]*([a-z])([a-z])\2\1[^\[\]]*\]', s))

  if not len(groups):
    return False

  for g in abbas:
    if g[0] == g[1]:
      continue

    if groups[g] - inners[g] > 0:
      continue
    return False

  return True

def find_abas(s):
  ins, outs = set(), set()
  inside = False
  for k in zip(s, s[1:], s[2:]):
    if len(k) < 3:
      continue
    if k[0] == '[':
      inside = True
      continue
    if k[0] == ']':
      inside = False
      continue

    if '[' in k or ']' in k:
      continue
    if k[0] == k[2] and k[1] != k[0]:
      (ins if inside else outs).add((k[0], k[1]))
  
  return outs, ins

def supports_licensing(s):
  outs, ins = find_abas(s)

  print(s, outs, ins)

  for out in outs:
    if out[::-1] in ins:
      return True

  return False

def main(raw, part):
  total = 0

  data = processInput(raw)

  if part == 1:
    for ip in data:
      works = supports_snoop(ip)
      total += int(works)
      
    return total
  elif part == 2:
    for ip in data:
      works = supports_licensing(ip)
      if len(data) < 20:
        print(ip, works)
      total += int(works)
      
    return total

if __name__ == '__main__':
  part1_sample = main(readFileName('s.txt'), 1)
  print('Part 1 (sample):', part1_sample)
  assert part1_sample == 2

  part1_real = main(readFileName('r.txt'), 1)
  print('Part 1 (real):', part1_real)
  assert part1_real == 115

  part2_sample = main(readFileName('s2.txt'), 2)
  print('Part 2 (sample):', part2_sample)
  assert part2_sample == 3

  part2_real = main(readFileName('r.txt'), 2)
  print('Part 2 (real):', part2_real)
  # assert part2_real == 0
