# Part 1
import utils as u

lines = u.readFile()

seq = lines[0].strip()

Map = {}
pos = 'AAA'

for line in lines[2:]:
  start, d = line.split(' = ')
  l,r = d[1:-1].split(', ')
  Map[start] = (l,r)

cnt = 0

while pos != 'ZZZ':
  nexts = Map[pos]
  newPos = nexts[1 if seq[cnt % len(seq)] == 'R' else 0]
  pos = newPos

  cnt += 1

print(cnt)
