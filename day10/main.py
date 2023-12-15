import utils as u

lines = [list(l.strip()) for l in u.readFile()]

output = [[' '] * len(line) * 3 for line in (lines * 3)]

total = 0

Map = {}
ss = set()

down = '|F7S'
up = '|JLS'
left = '-J7S'
right = '-FLS'

startRC = (0, 0)
for val, rrr, row in u.enumerateGrid(lines):
  if val == 'S':
    startRC = rrr

def valid_move(rc1, rc2):
  c1 = lines[rc1[0]][rc1[1]]
  c2 = lines[rc2[0]][rc2[1]]

  if rc1[0] < rc2[0]:
    # Above
    return c1 in down and c2 in up
  elif rc1[1] < rc2[1]:
    # going Right
    return c1 in right and c2 in left
  elif rc1[0] > rc2[0]:
    # going up
    return c1 in up and c2 in down
  elif rc1[1] > rc2[1]:
    # going left
    return c1 in left and c2 in right

def valid2(rc1, rc2):
  c1 = lines[rc1[0]][rc1[1]]
  c2 = lines[rc2[0]][rc2[1]]

  if rc1[0] < rc2[0]:
    # Above
    return c1 in down and c2 in up
  elif rc1[1] < rc2[1]:
    # going Right
    return c1 in right and c2 in left
  elif rc1[0] > rc2[0]:
    # going up
    return c1 in up and c2 in down
  elif rc1[1] > rc2[1]:
    # going left
    return c1 in left and c2 in right

g = u.grid_to_graph(lines, valid_move, False)



seen,from_map = u.flood_fill(g, startRC)
print(seen, len(seen))

dist_map = {}
def compute_distance(current, target, from_map):
  if current in dist_map:
    return dist_map[current]
  if current == target:
    return 0
  p = from_map[current]
  if p == target:
    dist_map[current] = 1
    return 1
  

farthest = startRC
dist = 0
# for mine in seen:
#   d = u.bfs(g, startRC, lambda x: x == mine)
#   if len(d) > dist:
#     dist = len(d)
#     farthest = mine

relevant = {
  '-': '   xxx   ',
  '|': ' x  x  x ',
  'J': ' x xx    ',
  'L': ' x  xx   ',
  '7': '   xx  x ',
  'F': '    xx x ',
  'S': ' x xxx x ',
}

for v,rc,row in u.enumerateGrid(lines):
  r,c = rc
  if rc in seen:
    # lines[r][c] = '#'
    myline = list(relevant[v] or '!!!!!!!!!')
    for r2 in range(r * 3, r * 3 + 3):
      for c2 in range(c * 3, c * 3 + 3):
        char = myline.pop(0)
        output[r2][c2] = char
    pass
  else:
    lines[r][c] = '.' if lines[r][c] == '.' else ' '
    # if lines[r][c] == '.':
    output[r*3+1][c*3+1] = '#'
    # lines[r][c] = '.'
  # if lines[r][c] in '0123456789':
  #   tgrid[r][c] = '7'
  # elif lines[r][c] != '.':
  #   tgrid[r][c] = '*'
  # elif not rc in seen:
  #   tgrid[rc[0]][rc[1]] = '_'
  # else:
  #   tgrid[rc[0]][rc[1]] = ' '
print('\n'.join(''.join(c for c in row) for row in lines))

# processing??
print(farthest, dist - 1)
# print('Total:', total)

def valid3(rc1, rc2):
  c1 = output[rc1[0]][rc1[1]]
  c2 = output[rc2[0]][rc2[1]]
  return c1 != 'x' and c2 != 'x'

total9 = 0

seen23, from_map2 = u.flood_fill(u.grid_to_graph(output, valid3, False), (0, 0))

for v, rc6, row in u.enumerateGrid(output):
  if v == '#' and rc6 not in seen23:
    total9 += 1

  if rc6 not in seen23:
    if v == 'x':
      row[rc6[1]] = '|'
    elif v == ' ':
      row[rc6[1]] = ' '
  else:
    row[rc6[1]] = ' '

print('\n'.join(''.join(c for c in row) for row in output))


print(total9)