from utils import *
import re
import sys

sys.setrecursionlimit(1000)

def processInput(data):
  return data[0]

def get_length(sequence):
  if '(' not in sequence or ')' not in sequence:
    return len(sequence)

  first_open = sequence.index('(')
  first_close = sequence.index(')')
  
  group = sequence[first_open+1:first_close]
  width, repeats = map(int, group.split('x'))

  return first_open + width * repeats + get_length(sequence[first_close + 1 + width:])

def get_result(sequence):
  if '(' not in sequence or ')' not in sequence:
    return len(sequence)

  first_open = sequence.index('(')
  first_close = sequence.index(')')
  
  group = sequence[first_open+1:first_close]
  width, repeats = map(int, group.split('x'))

  return len(sequence[:first_open]) + \
    get_result(sequence[first_close + 1:first_close + 1 + width]) * repeats + \
    get_result(sequence[first_close + 1 + width:])


def main(raw, part):
  total = 0

  data = processInput(raw)

  if part == 1:
    return get_length(data)
  elif part == 2:
    return get_result(data)

if __name__ == '__main__':
  test('p1 s1', 7, main(readFileName('s.txt'), 1))
  test('p1 real', 120765, main(readFileName('r.txt'), 1))
  test('p2 s1', 7, main(readFileName('s.txt'), 2))
  test('p2 s1', 20, main(readFileName('s2.txt'), 2))
  test('p2 real', 0, main(readFileName('r.txt'), 2))
