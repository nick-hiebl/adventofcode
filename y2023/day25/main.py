from utils import *
import re
import networkx

def processInput(data):
  graph = networkx.Graph()

  for line in data:
    name, outs = line.split(': ')

    for out in outs.split(' '):
      graph.add_edge(name, out)

  return graph

def main(raw, part):
  total = 0

  graph = processInput(raw)

  if part == 1:
    res2 = networkx.minimum_edge_cut(graph)
    for edge in res2:
      graph.remove_edge(*edge)
    res = list(networkx.connected_components(graph))
    # print(res2)
    print(res)
    print([len(x) for x in res])

  elif part == 2:
    for cmd in data:
      pass
    return total

if __name__ == '__main__':
  part1_sample = main(readFileName('s.txt'), 1)
  print('Part 1 (sample):', part1_sample)
  # assert part1_sample == 0

  part1_real = main(readFileName('r.txt'), 1)
  print('Part 1 (real):', part1_real)
  assert part1_real == 0

  # part2_sample = main(readFileName('s.txt'), 2)
  # print('Part 2 (sample):', part2_sample)
  # assert part2_sample == 0

  # part2_real = main(readFileName('r.txt'), 2)
  # print('Part 2 (real):', part2_real)
  # # assert part2_real == 0
