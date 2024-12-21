from utils import *
import re
from functools import cache
from sys import setrecursionlimit

setrecursionlimit(10 ** 6)

NUMPAD = tuple('789 456 123 X0A'.split(' '))
DIRPAD = tuple('X^A <v>'.split(' '))

@cache
def find_pos(pad, key):
  for r, row in enumerate(pad):
    for c, cell in enumerate(row):
      if cell == key:
        return (r, c)
  assert False

DIRNS = {
  '>': (0, 1),
  '<': (0, -1),
  'v': (1, 0),
  '^': (-1, 0)
}

def verify(outpad, sequence):
  pos = find_pos(outpad, 'A')
  output = []
  for cha in sequence:
    if cha == 'A':
      output.append(outpad[pos[0]][pos[1]])
    else:
      pos = tadd(pos, DIRNS[cha])
  
  return output

@cache
def solve_for_x(outpad, sequence, pos):
  if len(sequence) == 0:
    return ('',)
  else:    
    nextp = find_pos(outpad, sequence[0])

    afters = solve_for_x(outpad, sequence[1:], nextp)

    mycombs = []

    if nextp[0] == pos[0]:
      if nextp[1] < pos[1]:
        commands = ['<'] * abs(nextp[1] - pos[1]) + ['A']
        mycombs.append(commands)
      elif nextp[1] > pos[1]:
        commands = ['>'] * abs(nextp[1] - pos[1]) + ['A']
        mycombs.append(commands)
      else:
        mycombs.append(['A'])
    elif nextp[1] == pos[1]:
      if nextp[0] < pos[0]:
        commands = ['^'] * abs(nextp[0] - pos[0]) + ['A']
        mycombs.append(commands)
      elif nextp[0] > pos[0]:
        commands = ['v'] * abs(nextp[0] - pos[0]) + ['A']
        mycombs.append(commands)
    else:
      horis = ('<' if nextp[1] < pos[1] else '>') * abs(nextp[1] - pos[1])
      verts = ('^' if nextp[0] < pos[0] else 'v') * abs(nextp[0] - pos[0])

      if outpad == NUMPAD:
        if outpad[pos[0]][nextp[1]] != 'X':
          mycombs.append(horis + verts + 'A')
        if outpad[nextp[0]][pos[1]] != 'X':
          mycombs.append(verts + horis + 'A')
      else:
        if outpad[pos[0]][nextp[1]] == 'X':
          mycombs.append(verts + horis + 'A')
        elif outpad[nextp[0]][pos[1]] == 'X':
          mycombs.append(horis + verts + 'A')
        else:
          mycombs.append(verts + horis + 'A')
          # mycombs.append(horis + verts + 'A')

    output = []
    for combo in mycombs:
      for z in solve_for_x(outpad, sequence[1:], nextp):
        output.append(''.join(combo) + z)
    return tuple(output)

@cache
def get_shortest_n2(sequence, pads):
  assert len(pads) > 0
  start = find_pos(pads[0], 'A')
  considers = []
  for s in solve_for_x(pads[0], sequence, start):
    considers.append(s)

  print('considers', len(considers))

  out = []
  for s in considers:
    if len(pads) == 1:
      # yield s
      out.append(s)
    else:
      for t in get_shortest_n2(s, pads[1:]):
        # yield t
        out.append(t)
  # print('ssss', len(pads), len(out), [len(x) for x in out], len(considers), [len(c) for c in considers])
  return tuple(out)

def shortestn2wrapper(sequence, pads):
  best = []
  bestlen = 10 ** 100
  for x in get_shortest_n2(sequence, tuple(pads)):
    if len(x) < bestlen:
      best = x
      bestlen = len(x)
  
  return best

def processInput(data):
  out = []

  for line in data:
    out.append(line)

  return out

def main(raw, part):
  total = 0

  data = processInput(raw)

  pads = [NUMPAD] + [DIRPAD] * 2

  if part == 2:
    pads = [NUMPAD] + [DIRPAD] * 9

  for cmd in data:
    b = shortestn2wrapper(cmd, pads)

    x,y = len(b), int(''.join(cha for cha in cmd if cha.isnumeric()))
    print(x,y)
    total += x * y
  return total

if __name__ == '__main__':
  test('p1 s1', 126384, main(readFileName('s.txt'), 1))
  test('p1 real', 202648, main(readFileName('r.txt'), 1))
  # test('p2 s1', 0, main(readFileName('s.txt'), 2))
  test('p2 real', 0, main(readFileName('r.txt'), 2))
