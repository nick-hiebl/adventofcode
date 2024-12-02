import utils as u
from itertools import combinations

lines = u.readFile()

total = 0

def canEmpty(s):
  return '#' not in s
def canFill(s):
  return '.' not in s

def ways_to_solve(cache, mystring, counts):
  assert len(counts) > 0

  key = (len(mystring), len(counts))
  if key in cache:
    return cache[key]

  me = counts[0]
  if len(counts) == 1:
    if len(mystring) < me:
      return 0
    ways = 0
    for j in range(0, len(mystring) - me + 1):
      if canFill(mystring[j:j+me]) and canEmpty(mystring[:j]) and canEmpty(mystring[j+me:]):
        ways += 1
    cache[key] = ways
    return ways

  must_leave = len(mystring) - sum(counts[1:]) - (len(counts) - 1)
  ways = 0

  for j in range(0, must_leave):
    now = mystring[j:j+me]
    before = mystring[:j]
    after = '' if len(mystring) <= (j+me) else mystring[j+me]
    if canFill(now) and canEmpty(before) and canEmpty(after):
      ways += ways_to_solve(cache, mystring[j+me+1:], counts[1:])
  cache[key] = ways
  return ways

for i,line in enumerate(lines):
  sss,c__ = line.split(' ')
  springs = '?'.join([sss] * 5)
  cs = [int(c) for c in c__.split(',')] * 5

  print(i, springs, cs)

  cache = {}
  t = ways_to_solve(cache, springs, cs)

  total += t

print('Total:', total)
