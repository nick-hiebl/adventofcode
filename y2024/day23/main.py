from utils import *
import re
import networkx
from collections import defaultdict, deque

def process2(data):
  graph = networkx.Graph()

  for line in data:
    a,b = line.split('-')
    graph.add_edge(a, b)
    graph.add_edge(b, a)
  return graph

def processInput(data):
  graph = defaultdict(set)

  for line in data:
    a,b = line.split('-')
    graph[a].add(b)
    graph[b].add(a)

  return graph

def group_of_size_from_start(n, graph, lads, start):
  friends = set(f for f in lads if f in graph[start])
  friends.add(start)
  print('My friends', n, start, friends)

  if len(friends) < n:
    return False

  to_check = list(friends)
  for i in to_check:
    if len(friends) < n:
      return False
    
    friends = set(f for f in friends if f == i or f in graph[i])
    friends.add(i)
  
  return len(friends) >= n

def has_group_of_size(n, graph):
  big_lads = set(k for k in graph.keys() if len(graph[k]) >= n)
  print(big_lads)

  banned = set()

  if len(big_lads) < n:
    return False
  
  it = list(big_lads)
  for node in it:
    if node not in big_lads:
      continue
    if len(big_lads) < n:
      return False

    if group_of_size_from_start(n, graph, big_lads, node):
      return True

    big_lads.remove(node)
  
  return False

def main(raw, part):
  total = 0

  graph = processInput(raw)

  if part == 1:
    groups = set()
    for node in graph.keys():
      if node.startswith('t'):
        for nb in graph[node]:
          for nc in graph[node]:
            if nc in graph[nb]:
              groups.add(tuple(sorted([node, nb, nc])))

    return len(groups)
  elif part == 2:
    g2 = process2(raw)


    cl = max(networkx.find_cliques(g2), key=len)

    nodes = ','.join(sorted(list(cl)))
    return nodes


if __name__ == '__main__':
  test('p1 s1', 7, main(readFileName('s.txt'), 1))
  test('p1 real', 1248, main(readFileName('r.txt'), 1))
  test('p2 s1', 'co,de,ka,ta', main(readFileName('s.txt'), 2))
  test('p2 real', 'aa,cf,cj,cv,dr,gj,iu,jh,oy,qr,xr,xy,zb', main(readFileName('r.txt'), 2))
