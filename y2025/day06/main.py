from utils import *
import re

def processInput(data):
  numbers = []
  operands = []

  for line in data:
    row = line.split(' ')

    if '+' in row:
      operands = [v for v in row if v]
    else:
      numbers.append(list(int(x) for x in row if x))

  return list(zip(*numbers)), operands

def fix(nums, operand):
  if operand == '+':
    return sum(nums)
  else:
    r = 1
    for n in nums:
      r *= n
    return r

def processInput2(data):
  problems = []
  nums = []
  operand = ''
  for r in zip(*data):
    r = tuple(' ' if x == '\n' else x for x in r)
    if all(v == ' ' for v in r):
      problems.append((nums, operand))
      nums = []
      operand = ''
      continue

    if r[-1] in ('+', '*'):
      operand = r[-1]
    
    num = int(''.join(r[:-1]).replace(' ', ''))
    nums.append(num)

  return problems

def main(raw, part):
  total = 0


  if part == 1:
    numbers, operands = processInput(raw)

    print(numbers, operands)
    for row, operand in zip(numbers, operands):
      total += fix(row, operand)
    return total
  elif part == 2:
    problems = processInput2(raw)[::-1]
    for nums, operand in problems:
      total += fix(nums, operand)
    return total

if __name__ == '__main__':
  test('p1 s1', 4277556, main(readFileName('s.txt'), 1))
  test('p1 real', 5316572080628, main(readFileName('r.txt'), 1))
  test('p2 s1', 3263827, main(readFileName_nostrip('s.txt'), 2))
  test('p2 real', 0, main(readFileName_nostrip('r.txt'), 2))
