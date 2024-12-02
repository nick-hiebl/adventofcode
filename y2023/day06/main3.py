# THIS IS NOT THE REAL ORIGINAL ATTEMPT

import sys
import re
print(sys.argv)

with open(sys.argv[1], 'r') as f:
  lines = [l.strip() for l in f.readlines()]

# print(lines)
[timeL, distL] = lines

times = [int(x) for x in timeL.replace(' ', '').split(':')[1].strip().split(' ') if x]
dists = [int(x) for x in distL.replace(' ', '').split(':')[1].strip().split(' ') if x]

total = 1

print(times, dists)

def possible(t, d, w):
  r_t = t - w
  speed = w
  return r_t * speed > d

def try_range(t, d, l, h):
  twstep = int((h - l) * 0.03)
  for j in range(l, h, twstep if twstep > 0 else 1):
    print(j, possible(t, d, j))
# 14 works
# 71517 dont

# 5330503 works

#5074868 7612302
#43136378 45673812

for i in range(len(times)):
  t = times[i]
  d = dists[i]
  ways = 0

  lo = int((t - (t * t - 4 * d) ** 0.5) / 2)
  hi = int((t + (t * t - 4 * d) ** 0.5) / 2)
  print(lo, hi)
  print(hi - lo)
      
  print(ways)
  # total *= ways

print(total)
