import utils as u

lines = u.readFile()

nex = { '>': (0, 1), 'v': (1, 0), '<': (0, -1), '^': (-1, 0) }

a = (0, 0)
b = (0, 0)
visited = set()
visited.add(a)

for c,d in u.bundle(lines[0].strip()):
  a = u.tadd(a, nex[c])
  b = u.tadd(b, nex[d])
  visited.add(a)
  visited.add(b)

print(len(visited))
