from utils import *
import re

def processInput(data):
  out = []

  for line in data:
    out.append(line)

  return out

def main(raw, part):
  total = 0

  data = processInput(raw)

  if part == 1:
    for cmd in data:
      pass
    return total
  elif part == 2:
    for cmd in data:
      pass
    return total

if __name__ == '__main__':
  test('p1 s1', 0, main(readFileName('s.txt'), 1))
  test('p1 real', 0, main(readFileName('r.txt'), 1))
  test('p2 s1', 0, main(readFileName('s.txt'), 2))
  test('p2 real', 0, main(readFileName('r.txt'), 2))
