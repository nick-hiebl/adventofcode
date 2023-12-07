import sys
import re
print(sys.argv)

with open(sys.argv[1], 'r') as f:
  lines = [l.strip() for l in f.readlines()]

# print(lines)
[timeL, distL] = lines

times = [int(x) for x in timeL.split(':')[1].strip().split(' ') if x]
dists = [int(x) for x in distL.split(':')[1].strip().split(' ') if x]

total = 1

for i in range(len(times)):
  t = times[i]
  d = dists[i]

  ways = 0
  for j in range(t):
    r_t = t - j
    speed = j
    if r_t * speed > d:
      ways += 1
  print(ways)
  total *= ways

print(total)
