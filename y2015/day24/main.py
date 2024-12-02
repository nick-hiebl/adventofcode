from utils import *

def processInput(data):
  out = []

  for line in data:
    out.append(int(line))

  return out

def knapsack(soln, target):
  print('computing', soln, target)
  grid = [[None] * (target + 1) for _ in soln]

  for index, w in enumerate(soln):
    if index > 0:
      for prev, value in enumerate(grid[index - 1]):
        if not value:
          continue

        grid[index][prev] = value


    if grid[index][w]:
      grid[index][w] = min(grid[index][w], (1, w, [w]))
    else:
      grid[index][w] = (1, w, [w])
    
    if index > 0:
      for prev, items in enumerate(grid[index - 1]):
        if items and prev + w <= target:
          if grid[index][prev + w]:
            grid[index][prev + w] = min(grid[index][prev + w], (items[0] + 1, items[1] * w, items[2] + [w]))
          else:
            grid[index][prev + w] = (items[0] + 1, items[1] * w, items[2] + [w])
    
    print('Best so far (after {} [{}]): {}'.format(index, w, grid[index][-1]))
  
  # printGrid(zip(*grid))
  return grid[-1][-1]


def main(raw, part):
  total = 0

  data = processInput(raw)

  if part == 1:
    return knapsack(data, sum(data) // 3)[1]
  else:
    return knapsack(data, sum(data) // 4)[1]

if __name__ == '__main__':
  part1_sample = main(readFileName('s.txt'), 1)
  print('Part 1 (sample):', part1_sample)
  assert part1_sample == 99

  part1_real = main(readFileName('r.txt'), 1)
  print('Part 1 (real):', part1_real)
  assert part1_real == 10723906903

  part2_sample = main(readFileName('s.txt'), 2)
  print('Part 2 (sample):', part2_sample)
  assert part2_sample == 44

  part2_real = main(readFileName('r.txt'), 2)
  print('Part 2 (real):', part2_real)
  # assert part2_real == 0
