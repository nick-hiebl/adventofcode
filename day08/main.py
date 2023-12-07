# Part 2
import utils as u
import math

lines = u.readFile()

seq = lines[0].strip()

Map = {}
nows_0 = []

for line in lines[2:]:
  start, d = line.split(' = ')
  if start[-1] == ('A'):
    nows_0.append(start)
  l,r = d[1:-1].split(', ')
  Map[start] = (l,r)

## <ADDED AFTER>
cnts = []
## </ADDED AFTER>

for n in nows_0:
  cnt = 0
  nextSet = set()
  nows = [n]
  while not all(x[-1] == ('Z') for x in nows):
    newInd = 1 if seq[cnt % len(seq)] == 'R' else 0
    nextSet = set()
    for node in nows:
      nextSet.add(Map[node][newInd])
    
    cnt += 1
    nows = list(nextSet)
    # print(cnt, len(nows))
  print(n, cnt)
  ## <ADDED AFTER>
  cnts.append(cnt)
  print('-'.join(path))
  ## </ADDED AFTER>

print(cnt)

## <ADDED AFTER>

##### During the actual challenge I did this manually in the console with the output from line 36 above
print('answer:', math.lcm(*cnts))
print('all divisible:', all(x == math.lcm(x, len(seq)) for x in cnts))
## </ADDED AFTER>
