import utils as u

lines = [(int(x), i) for i,x in enumerate(u.readFile())]

def find(ls, i):
  for index,l in enumerate(ls):
    if l[1] == i:
      return (index,l)

def findV(ls, v):
  for index,l in enumerate(ls):
    if l[0] == v:
      return index

def mix(ls):
  for i in range(len(ls)):
    index,v = find(ls, i)
    new_index = (index + (v[0] % len(ls)) + 100 * len(ls)) % len(ls) - (1 if v[0] < 0 else 0)
    # print('  > considering:', v[0], 'which was at:', index, 'now going to:', new_index)
    ls.remove(v)
    ls.insert(new_index, v)
    # print([x for x,y in ls])

  return ls

# print([x for x,y in lines])
v = mix(lines)

print([x for x,y in v])
z = findV(v, 0)
print(sum([v[(z + x) % len(v)][0] for x in [1000, 2000, 3000]]))
