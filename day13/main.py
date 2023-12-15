import utils as u

ls = u.readFile()

total = 0

l2 = '\n'.join(ls)
gs = l2.split('\n\n')

groups = [l.split('\n') for l in gs]

print(groups)

def mirrorsOn(row, x):
  e = min(x, len(row) - x)
  return row[x-e:x+e] == (row[x-e:x+e])[::-1]

def mirrorErrors(grid, x):
  e = min(x, len(grid[0]) - x)
  errors = 0
  for row in grid:
    splice = row[x-e:x+e]
    errors += sum(1 if a != b else 0 for a,b in zip(splice, splice[::-1]))
  print(x, 'Errors:', errors)
  return errors // 2

def transpose(g):
  return [''.join(g[i][j] for i in range(len(g))) for j in range(len(g[0]))]

for group in groups:
  l = list(i for i in range(1, len(group[0])) if mirrorErrors(group, i) == 1)
  # for row in group:
  #   l = [x for x in l if mirrorsOn(row, x)]

  print(l)
  total += sum(l)

  g2 = transpose(group)
  l = list(i for i in range(1, len(g2[0])) if mirrorErrors(g2, i) == 1)
  # for row in g2:
  #   l = [x for x in l if mirrorsOn(row, x)]
  
  print(l)
  total += 100 * sum(l)



print('Total:', total)
