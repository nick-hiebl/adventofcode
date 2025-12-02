from utils import *
import re

def processInput(data, part):
  pos = 50
  SIZE = 100
  count = 0
  clicks = 0

  for line in data:
    if line.startswith('L'):
      jump = int(line[1:])
      clicks += jump // SIZE
      jump = jump % SIZE
      if pos > 0 and jump >= pos:
        clicks += 1
      pos = (pos - jump + SIZE * 10) % SIZE
    else:
      jump = int(line[1:])
      clicks += jump // SIZE
      jump = jump % SIZE
      if pos + jump >= SIZE:
        clicks += 1
      pos = (pos + jump) % SIZE
    
    if pos == 0:
      count += 1

  if part == 1:
    return count
  return clicks

def main(raw, part):
  total = 0

  count = processInput(raw, part)

  if part == 1:
    return count
  elif part == 2:
    return count

if __name__ == '__main__':
  test('p1 s1', 3, main(readFileName('s.txt'), 1))
  test('p1 real', 1066, main(readFileName('r.txt'), 1))
  test('p2 s1', 8, main(readFileName('s.txt'), 2))
  test('p2 real', 6223, main(readFileName('r.txt'), 2))
