from utils import *
import re

def processInput(commands, X, Y):
  data = [[False] * X for i in range(Y)]

  for command in commands:
    if command.startswith('rect'):
      dim = command.split(' ')[1]
      w,h = map(int, dim.split('x'))
      print('Rect', w, h)
      for row in range(min(h, Y)):
        for col in range(min(w, X)):
          data[row][col] = True
    else:
      r, drn, place, _, offs = command.split(' ')
      print('rotate', drn, place, offs)
      iden = int(place.split('=')[1])
      offset = int(offs) % X if drn == 'row' else int(offs) % Y
      if drn == 'row':
        row = data[iden]
        data[iden] = row[-offset:] + row[:-offset]
      else:
        col = [data[i][iden] for i in range(len(data))]
        col = col[-offset:] + col[:-offset]
        for y in range(len(data)):
          data[y][iden] = col[y]
    printGrid(data, lambda x: '#' if x else '.')

  print(list(sum(1 if v else 0 for v in row) for row in data))
  return sum(sum(1 if v else 0 for v in row) for row in data)

def main(raw, sample, part):
  total = 0

  data = processInput(raw, 50 if sample == 2 else 7, 6 if sample == 2 else 3)

  if part == 1:
    return data
  elif part == 2:
    return data

if __name__ == '__main__':
  test('p1 s1', 6, main(readFileName('s.txt'), 1, 1))
  test('p1 real', 0, main(readFileName('r.txt'), 2, 1))
  # Look at the output from above to see what the appropriate string is
  # test('p2 s1', 0, main(readFileName('s.txt'), 1, 2))
  # test('p2 real', 0, main(readFileName('r.txt'), 2, 2))
