import utils as u

lines = u.readFile()

g = [[0 for i in range(1000)] for j in range(1000)]

def tocoords(a):
  return tuple(int(x) for x in a.split(','))

for line in lines:
  ws = line.split(' ')
  bl = tocoords(ws[-3])
  tr = tocoords(ws[-1])
  i = ws[0:2]
  for r in range(bl[0], tr[0] + 1):
    for c in range(bl[1], tr[1] + 1):
      
      if ws[0] == 'toggle':
        g[r][c] = g[r][c] + 2
      elif ws[1] == 'on':
        g[r][c] = g[r][c] + 1
      else:
        g[r][c] = max(0, g[r][c] - 1)

print(sum(sum(r) for r in g))
