from utils import *
import re
from functools import cache

def processInput(data):
  patterns = []
  desired = []

  for line in data:
    if ',' in line:
      patterns = line.split(', ')
    elif line:
      desired.append(line)

  return tuple(patterns), desired

@cache
def is_possible(goal, patterns):
  if len(goal) == 0 or goal in patterns:
    return True
  
  for p in patterns:
    if goal.startswith(p):
      if is_possible(goal[len(p):], patterns):
        return True
  
  return False

@cache
def num_ways(goal, patterns):
  if len(goal) == 0:
    return 1
  
  ways = 0
  
  for p in patterns:
    if goal == p:
      ways += 1
    elif goal.startswith(p):
      child = num_ways(goal[len(p):], patterns)
      ways += child
  
  return ways

def main(raw, part):
  total = 0

  patterns, desired = processInput(raw)

  if part == 1:
    for i,desire in enumerate(desired):
      # print(i)
      if is_possible(desire, patterns):
        total += 1
    return total
  elif part == 2:
    for i,desire in enumerate(desired):
      # print(i)
      total += num_ways(desire, patterns)
    return total

if __name__ == '__main__':
  test('p1 s1', 6, main(readFileName('s.txt'), 1))
  test('p1 real', 365, main(readFileName('r.txt'), 1))
  test('p2 s1', 16, main(readFileName('s.txt'), 2))
  test('p2 real', 730121486795169, main(readFileName('r.txt'), 2))
