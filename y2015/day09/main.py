import utils as u
import itertools

lines = u.readFile()

Map = {}

cities = set()

for line in lines:
  a,_,b,__,d = line.split()
  start = Map.get(a, {})
  Map[a] = start
  start[b] = int(d)
  end = Map.get(b, {})
  Map[b] = end
  end[a] = int(d)
  cities.add(a)
  cities.add(b)

best = 0
cities = list(cities)

def try_forward(c, been_to = set()):
  if len(been_to) == len(cities):
    return 0
  if c not in Map:
    return best - 10
  ops = []
  for op in Map[c].keys():
    if op in been_to:
      continue
    been_to.add(op)
    ops.append(Map[c][op] + try_forward(op, been_to))
    been_to.remove(op)
  return max(ops)

# for perm in itertools.permutations(cities, r=len(cities)):
#   d = 0
#   for i in range(len(perm) - 1):
#     a,b = perm[i],perm[i+1]
#     if not a in Map or not b in Map[a]:
#       d = best + 10
#       break
#     d += Map[a][b]
#   best = min(d, best)
#   print(d, perm)

for c in Map.keys():
  best = max(best, try_forward(c, {c}))

print(best)
