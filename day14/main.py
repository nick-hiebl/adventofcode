import utils as u

lines = u.readFile()

total = 0

def transpose(t):
  return tuple([*zip(*t)])

cols = transpose(lines)

def rollUp(grid):
  result = []
  for col in grid:
    balls = 0
    space = 0

    out = ''

    for c in col:
      if c == '.':
        space += 1
      elif c == 'O':
        space += 1
        balls += 1
      elif c == '#':
        out += balls * 'O' + (space - balls) * '.' + '#'
        balls = 0
        space = 0
    out += balls * 'O' + (space - balls) * '.'

    result.append(out)
  return tuple(result)

def rotate(grid):
  return transpose(grid)[::-1]

def runCycle(g):
  for i in range(4):
    g = rollUp(g)
    g = rotate(g)
  return g

def show(g):
  print('\n'.join(''.join(c for c in row) for row in g))

def computeStress(g):
  total = 0
  for col in g:
    for i,c in enumerate(col):
      if c == 'O':
        total += len(col) - i
  return total

def detectCycle(initial, step, cycles):
  seen = {}
  seen[initial] = 0
  s = initial
  for i in range(1, cycles):
    s = step(s)
    if s in seen:
      last = seen[s]
      now = i
      loop = now - last
      for j in range((cycles - last) % loop):
        s = step(s)
      return s
    seen[s] = i

stresses = []

seen = {}

MAGIC_NUMBER = 1000000000 #1000000000
correct_answer = 97241
state = cols
# repeated = 0
# looping = False
# for i in range(1005):
#   state = runCycle(state)
#   stresses.append(computeStress(state))
#   x = '\n'.join(''.join(c for c in row) for row in state)
  
#   if x in seen:
#     lastSeen = seen[x]
#     loopLen = i - lastSeen

#     endpoint = (MAGIC_NUMBER - lastSeen) % loopLen + lastSeen
#     end = MAGIC_NUMBER
#     j = end % loopLen
#     # print('j', j, loopLen)
#     print('Correct answer:', stresses[(end - lastSeen) % loopLen + lastSeen - 1])

#     # print(lastSeen, i, loopLen, endpoint)
#     # print(stresses[endpoint])
#     # print('Looped', i, seen[x])
#     break
#   seen[x] = i

s = detectCycle(state, runCycle, MAGIC_NUMBER)

print(computeStress(s))

# print('KEY', stresses[MAGIC_NUMBER - 1])

# print(result)
toShow = transpose(state)
# print(orig)
# show(toShow)
# print('Total:', stresses[-1])
# print(stresses)

