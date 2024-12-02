# THIS IS NOT THE REAL ORIGINAL ATTEMPT

import utils as u

lines = u.readFile()

# print(lines)

seeds = [int(x) for x in lines.pop(0).split(': ')[1].split(' ')]
# print(seeds)

f = ''
t = ''

stages = []

for line in lines:
  if 'map:' in line:
    f,t = line.split(' ')[0].split('-to-')
    stages.append((f,t,[]))
  elif f and line:
    dest, src, l = [int(x) for x in line.split(' ')]
    stages[-1][2].append((dest,src,l))

seedGs = u.bundle(seeds)
current = [(x, x+y) for x,y in seedGs]

for f,t,groups in stages:
  nextGs = []

  unpassedGs = current
  for dest,src,l in groups:
    left = []
    for g in unpassedGs:
      matched, unmatched = u.rangeFilter(g, (src, src+l))
      if matched:
        nextGs.append((matched[0] + dest - src, matched[1] + dest - src))
      left += unmatched
    unpassedGs = left

  current = nextGs + unpassedGs

print(min(min(c) for c in current))