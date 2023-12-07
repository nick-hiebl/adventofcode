import utils as u

lines = u.readFile()

allowable_cells = set(rc for c,rc,__ in u.enumerateGrid(lines) if c == '.' and any(v in '*/+$@%-&=0123456789' for v,rc2 in u.walkNeighbours(lines, *rc)))

g = u.grid_to_graph(lines, lambda x,y: x in allowable_cells and y in allowable_cells, False)
path = u.bfs(g, (0, 0), lambda x: x[0] == 139 and x[1] > 138) # == (139, 112))

tgrid = [list(j) for j in lines]

seen,x = u.flood_fill(g, (0, 0))

for v,rc,row in u.enumerateGrid(tgrid):
  r,c = rc
  if lines[r][c] in '0123456789':
    tgrid[r][c] = '7'
  elif lines[r][c] != '.':
    tgrid[r][c] = '*'
  elif not rc in seen:
    tgrid[rc[0]][rc[1]] = '_'
  else:
    tgrid[rc[0]][rc[1]] = ' '

for r,c in path:
  tgrid[r][c] = '∏'

print((1, 0) in seen)

print('\n'.join(''.join(r) for r in tgrid))
