import utils as u
import sys

raws = [int(x) for x in u.readFile()]
L = len(raws) - 1
jumps = [((j % L) + L * 10) % L - (0 if j < 0 else 0) for j in raws]

# print(['{} jumps by {}'.format(r,j) for r,j in zip(raws, jumps)])
order = list(range(len(raws)))

CORRECT = '''1, 2, -3, 3, -2, 0, 4
2, 1, -3, 3, -2, 0, 4
1, -3, 2, 3, -2, 0, 4
1, 2, 3, -2, -3, 0, 4
1, 2, -2, -3, 0, 3, 4
1, 2, -3, 0, 3, 4, -2
1, 2, -3, 0, 3, 4, -2
1, 2, -3, 4, 0, 3, -2'''

def mix(o, i):
  index = o.index(i)
  new_index = (index + jumps[i]) % L
  # print('     aaaa', index, jumps[i], L, new_index)
  if new_index == 0 and index != 0:
    new_index = L
  # if new_index < index:
  #   new_index += 1
  # print('  > considering:', raws[i], 'which was at:', index, 'now going to:', new_index)
  o.remove(i)
  o.insert(new_index, i)

  # SOUT = ', '.join(str(raws[i_]) for i_ in o)
  # print(SOUT)
  # COUT = CORRECT.split('\n')[i + 1]
  # if SOUT != COUT:
  #   print(i, SOUT, COUT)
  #   assert SOUT == COUT

def mix_all(o):
  for i in range(len(o)):
    mix(o, i)

# print([raws[i] for i in order])

# print([x for x,y in lines])
mix_all(order)

zero = order.index(raws.index(0))

def xyz(l):
  print(sum(l), l)

xyz([raws[order[(zero + pos) % len(order)]] for pos in [1000, 2000, 3000]])
# print([raws[i] for i in v])
# z = findV(v, 0)
# print(sum([v[(z + x) % len(v)][0] for x in [1000, 2000, 3000]]))
