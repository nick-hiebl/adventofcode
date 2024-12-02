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

current = seeds[:]

for f,t,groups in stages:
  over = []
  for seed in current:
    for dest,src,l in groups:
      if seed in range(src, src+l):
        over.append(seed + dest - src)
        break
    else:
      over.append(seed)
  current = over

print(current)
print(min(current))
