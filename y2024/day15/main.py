from utils import *
import re

DIRNS = {
  '<': (0, -1),
  '>': (0, 1),
  'v': (1, 0),
  '^': (-1, 0),
}

UNDIRNS = {
  (0, -1): '<',
  (0, 1): '>',
  (1, 0): 'v',
  (-1, 0): '^',
}

def processInput(data):
  path = []
  grid = []

  for line in data:
    if '#' in line:
      grid.append(line)
    elif 'v' in line or '>' in line:
      path += [DIRNS[c] for c in line]

  return path, grid

def processInput2(data):
  path = []
  grid = []
  for line in data:
    if '#' in line:
      grid.append(line.replace('#', '##').replace('O', '[]').replace('.', '..').replace('@', '@.'))
    elif 'v' in line or '>' in line:
      path += [DIRNS[c] for c in line]

  return path, grid

def boxes_grid2(grid):
  walls = []
  boxes = set()
  start = tuple()

  for r, row in enumerate(grid):
    for c, cell in enumerate(row):
      if cell == '[':
        boxes.add((r, c))
      elif cell == '@':
        start = (r, c)
    walls.append(row.replace('[', '.').replace(']', '.').replace('@', '.'))

  return walls, boxes, start

def boxes_grid(grid):
  walls = []
  boxes = set()
  start = tuple()

  for r, row in enumerate(grid):
    for c, cell in enumerate(row):
      if cell == 'O':
        boxes.add((r, c))
      elif cell == '@':
        start = (r, c)
    walls.append(row.replace('O', '.').replace('@', '.'))
  
  return walls, boxes, start

def show_state(pos, boxes, walls):
  print('\n'.join(''.join('@' if (r,c) == pos else 'O' if (r,c) in boxes else cell for c, cell in enumerate(row)) for r, row in enumerate(walls)))

def show_state2(pos, boxes, walls):
  print('\n'.join(''.join('@' if (r,c) == pos else '[' if (r,c) in boxes else ']' if (r,c-1) in boxes else cell for c, cell in enumerate(row)) for r, row in enumerate(walls)))

def move_state(start, boxes, walls, move):
  debug = move == (0, 10)
  next_pos = tadd(start, move)

  r,c = next_pos
  if walls[r][c] == '#':
    if debug:
      print('blocked by wall')
    return start

  if next_pos not in boxes:
    if debug:
      print('free space')
    return next_pos

  chain = next_pos
  while chain in boxes:
    chain = tadd(chain, move)
  if walls[chain[0]][chain[1]] == '#':
    return start
  else:
    boxes.remove(next_pos)
    boxes.add(chain)
    return next_pos

  return start

def find_boxes_to_move_vert(start, boxes, walls, move):
  assert move[1] == 0
  y_off = move[0]

  r,c = tadd(start, move)
  movers = []
  chain = [(r, c) if (r, c) in boxes else (r, c-1)]
  movers.append(chain[0])
  assert all(v in boxes for v in movers)

  while len(chain):
    after = []

    for r,c in chain:
      if walls[r + y_off][c] == '#' or walls[r + y_off][c+1] == '#':
        return False, []
      else:
        # Not blocked
        for off in [(y_off, -1), (y_off, 0), (y_off, 1)]:
          over = tadd((r,c), off)
          if over in boxes:
            if over not in after:
              after.append(over)
    
    movers += after
    chain = after
  
  return True, movers

def move_state2(start, boxes, walls, move):
  debug = move == (0, 10)
  next_pos = tadd(start, move)

  r,c = next_pos
  if walls[r][c] == '#':
    return start

  if move[1] == 0 and ((r,c) in boxes or (r,c-1) in boxes):
    can_do, movers = find_boxes_to_move_vert(start, boxes, walls, move)

    if not can_do:
      return start

    for b in movers:
      boxes.remove(b)
    
    for b in movers:
      boxes.add(tadd(b, move))

    return next_pos
  
  if next_pos not in boxes and (r, c-1) not in boxes:
    return next_pos

  chain = [(r, c) if (r, c) in boxes else (r, c-1)]
  assert chain[-1] in boxes

  works = True
  while True:
    last = chain[-1]
    following = tadd(last, (move[0], move[1] * 2))

    if following in boxes:
      chain.append(following)
    else:
      if move[1] == -1 and walls[following[0]][following[1]+1] == '#':
        works = False
      elif move[1] == 1 and walls[following[0]][following[1]] == '#':
        works = False
      break
  
  if not works:
    return start
  
  for c in chain[::-1]:
    boxes.remove(c)
    boxes.add(tadd(c, move))
  return next_pos

def main(raw, part):
  total = 0

  if part == 1:
    path, grid = processInput(raw)

    walls, boxes, start = boxes_grid(grid)

    pos = start
    for move in path:
      pos = move_state(pos, boxes, walls, move)
    
    for box in boxes:
      total += box[0] * 100 + box[1]
    
    return total
  elif part == 2:
    path, grid = processInput2(raw)
    walls, boxes, start = boxes_grid2(grid)

    pos = start

    for move in path:
      pos = move_state2(pos, boxes, walls, move)

    for box in boxes:
      total += box[0] * 100 + box[1]

    return total

if __name__ == '__main__':
  part1_sample = main(readFileName('s.txt'), 1)
  print('Part 1 (sample):', part1_sample)
  assert part1_sample == 10092

  part1_real = main(readFileName('r.txt'), 1)
  print('Part 1 (real):', part1_real)
  assert part1_real == 1516281

  part2_sample = main(readFileName('s.txt'), 2)
  print('Part 2 (sample):', part2_sample)
  assert part2_sample == 9021

  part2_real = main(readFileName('r.txt'), 2)
  print('Part 2 (real):', part2_real)
  assert part2_real == 1527969
