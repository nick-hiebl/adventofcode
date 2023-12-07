import utils as u
import math

lines = u.readFile()

seq = [0 if x == 'L' else 1 for x in lines[0].strip()]

Map = {}
starts = []

for line in lines[2:]:
  start, nexts = line.split(' = ')
  if start[-1] == 'A':
    starts.append(start)
  l,r = nexts[1:-1].split(', ')
  Map[start] = (l,r)

counts = []

def steps_to_end(start):
  cnt = 0
  while not start.endswith('Z'):
    start = Map[start][seq[cnt % len(seq)]]
    cnt += 1
  return cnt

def after_n(start, n):
  for i in range(n):
    start = Map[start][seq[cnt % len(seq)]]
  return start

print(math.lcm(*[steps_to_end(start) for start in starts]))
