import utils as u
import sys

raws = [int(x) * 811589153 for x in u.readFile()]
L = len(raws) - 1
jumps = [((j % L) + L * 10) % L - (0 if j < 0 else 0) for j in raws]

order = list(range(len(raws)))

def mix(o, i):
  index = o.index(i)
  new_index = (index + jumps[i]) % L
  if new_index == 0 and index != 0:
    new_index = L
  o.remove(i)
  o.insert(new_index, i)

def mix_all(o):
  for i in range(len(o)):
    mix(o, i)

# print([raws[i] for i in order])

# print([x for x,y in lines])
for _ in range(10):
  mix_all(order)

zero = order.index(raws.index(0))

def xyz(l):
  print(sum(l), l)

xyz([raws[order[(zero + pos) % len(order)]] for pos in [1000, 2000, 3000]])
# print([raws[i] for i in v])
# z = findV(v, 0)
# print(sum([v[(z + x) % len(v)][0] for x in [1000, 2000, 3000]]))
