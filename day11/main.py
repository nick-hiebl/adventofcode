import utils as u
import itertools

lines = u.readFile()

extraRows = []

for r,row in enumerate(lines):
  if not '#' in row:
    extraRows.append(r)

# for i in insertAfter[::-1]:
#   lines.insert(i, '.' * len(lines[0]))

extraCols = []

for c in range(len(lines[0])):
  if all(r[c] == '.' for r in lines):
    extraCols.append(c)

# for j in insertAt[::-1]:
#   for r,l in enumerate(lines):
#     lines[r] = l[:j] + '.' + l[j:]

print('\n'.join(lines))

stars = []

for v, rc, row in u.enumerateGrid(lines):
  if v == '#':
    stars.append(rc)

t = 0

factor = 1000000 - 1

print(len(extraRows), len(extraCols))

def dist(a,b):
  rs = range(min(a[0],b[0]), max(a[0],b[0]))
  cs = range(min(a[1],b[1]), max(a[1],b[1]))

  extraRs = [j for j in extraRows if j in rs]
  extraLs = [j for j in extraCols if j in cs]

  return abs(a[0] - b[0]) + abs(a[1] - b[1]) + len(extraRs) * factor + len(extraLs) * factor

j=0
for a,b in itertools.combinations(stars, r=2):
  t += dist(a,b)
  j+=1

print('total', t, j)
