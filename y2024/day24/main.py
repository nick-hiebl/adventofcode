from utils import *
import re
import random
import itertools
import networkx
import matplotlib.pyplot as plt

def processInput(data):
  definitions = {}
  states = {}

  for line in data:
    if ':' in line:
      key, val = line.split(': ')
      states[key] = int(val)
    elif '->' in line:
      dfn, key = line.split(' -> ')
      a, op, b = dfn.split(' ')
      definitions[key] = (a, op, b)

  return definitions, states

def processInput2(data):
  graph = networkx.DiGraph()

  for line in data:
    if '->' in line:
      dfn, key = line.split(' -> ')
      a, op, b = dfn.split(' ')
      # definitions[key] = (a, op, b)
      graph.add_edge(a, key)
      graph.add_edge(b, key)

  return graph

def rename_key(definitions, states, k1, k2):
  definitions[k2] = definitions[k1]

  del definitions[k1]

  for k in definitions.keys():
    a,op,b = definitions[k]
    if a == k1:
      definitions[k] = (k2, op, b)
    elif b == k1:
      definitions[k] = (a, op, k2)

def compute(definitions, states, key):
  if key in states:
    return states[key]
  
  a, op, b = definitions[key]

  av = compute(definitions, states, a)
  bv = compute(definitions, states, b)

  res = 0
  if op == 'AND':
    res = av & bv
  elif op == 'XOR':
    res = av ^ bv
  elif op == 'OR':
    res = av | bv
  else:
    assert False
  
  states[key] = res
  return res

def all_keys(definitions, states):
  return list(set(list(definitions.keys()) + list(states.keys())))

def all_keys_in(definitions, states, k):
  if k in definitions:
    a, _, b = definitions[k]
    return list(set([k] + all_keys_in(definitions, states, a) + all_keys_in(definitions, states, b)))
  else:
    return [k]

def parse_out(definitions, states, keystart):
  # print(keystart)
  # print(states)
  all_keys = list(set(list(definitions.keys()) + list(states.keys())))
  s = ''
  for k in sorted((k for k in all_keys if k.startswith(keystart)), reverse=True):
    s += str(compute(definitions, states, k))

  return int(s, 2)

def choose_n_pairs(options, num_pairs):
  if num_pairs == 0:
    yield []
  else:
    for a,b in itertools.combinations(options, 2):
      rest = set(options)
      rest.remove(a)
      rest.remove(b)
      for successors in choose_n_pairs(rest, num_pairs - 1):
        yield [(a,b)] + successors


renamers = {
  # ('A', 'AND', 'X'): ('B', 'lo'),
  # ('A', 'B', 'OR'): ('C', 'hi'),
  # ('AND', 'C', 'X'): ('D', 'hi'),
  # ('A', 'D', 'OR'): ('E', 'hi'),
  # ('AND', 'E', 'X'): ('C', 'hi'),
  ('A', 'AND', 'X'): ('B', 'hi'),
  ('A', 'B', 'OR'): ('C', 'hi'),
  ('AND', 'C', 'X'): ('B', 'hi'),
  ('C', 'X', 'XOR'): ('D', 'hi'),
  # ('A', 'D', 'OR'): ('E', 'hi'),
  # ('AND', 'E', 'X'): ('C', 'hi'),
}

def is_B_pair(definitions, k):
  if k.startswith('z'):
    return ''

  a, op, b = definitions[k]

  if not (a[1:].isnumeric() and b[1:].isnumeric()):
    return ''

  ns = sorted([a[1:], b[1:]])
  # print(ns)
  if abs(int(ns[0]) - int(ns[1])) > 1:
    return ''

  # print('Considering a potentially valid:', a, op, b, '->', k)
  
  new_code = tuple(sorted([a[0], b[0], op]))
  if new_code in renamers:
    pref, func = renamers[new_code]
    return pref + (min(ns) if func == 'lo' else max(ns))
  
  return ''


def main(raw, part):
  total = 0

  definitions, states = processInput(raw)

  if part == 1:
    return parse_out(definitions, states, 'z')
  elif part == 2:
    # # my_keys = ['x{:02d}'.format(i) for i in range(45)] + ['y{:02d}'.format(i) for i in range(45)]

    # # fine_keys = ['z00', 'z01', 'z02', 'z03', 'z04', 'z05', 'z06', 'z07', 'z08', 'z35', 'z36', 'z37', 'z38', 'z39', 'z40', 'z41', 'z42', 'z43', 'z44']
    # # under_fine_keys = set(sum((all_keys_in(definitions, states, k) for k in fine_keys), []))
    # # print('aaa', fine_keys, under_fine_keys)
    # # print(len(all_keys(definitions, states)))
    # # possibly_bad_keys = list(k for k in all_keys(definitions, states) if k not in under_fine_keys)
    # # print(len(possibly_bad_keys))

    # original = definitions.copy()

    # x = parse_out(definitions, states, 'x')
    # y = parse_out(definitions, states, 'y')

    # i = 0
    # # print(len(list(itertools.combinations(possibly_bad_keys,2))))
    # for a,b in itertools.combinations(all_keys(original, states), 2):
    #   if not (a in definitions and b in definitions):
    #     continue
    #   i += 1
    #   defs = original.copy()
    #   for a,b in [(a,b)]:
    #     temp = defs[a]
    #     defs[a] = defs[b]
    #     defs[b] = temp
      
    #   try:
    #     z = parse_out(defs, states, 'z')
    #     xy = x + y
    #     if x + y == z:
    #       print(pair_list)
    #       return -1
    #   except:
    #     print('Failed', i)
    #     continue
    #   if i % 1000 == 0:
    #     print(i)

    # return 2

    # for i in range(3):
    #   x = parse_out(definitions, states, 'x')
    #   y = parse_out(definitions, states, 'y')
    #   z = parse_out(definitions, states, 'z')
    #   xn = '{0:045b}'.format(x)
    #   yn = '{0:045b}'.format(y)
    #   zn = '{0:045b}'.format(z)
    #   xyn = '{0:045b}'.format(x + y)

    #   for i, (a,b,c,d) in enumerate(zip(xn[::-1], yn[::-1], xyn[::-1], zn[::-1])):
    #     in_this_row = sorted(list(k for k in all_keys_in(definitions, states, 'z{:02d}'.format(i)) if k not in under_fine_keys))
    #     print('{:02d}: {} {} {} {}'.format(i, a, b, c, d) , in_this_row, '----',)# under_fine_keys)

    #   print('    x =  {0:b}'.format(x))
    #   print('    y =  {0:b}'.format(y))
    #   print('x + y = {0:b}'.format(x + y))
    #   print('    z = {0:b}'.format(z))

    #   states = {}

    #   for k in my_keys:
    #     states[k] = random.randint(0, 1)
    # return -1

    # options = ['bbq', 'fsn', 'gsj', 'jjn', 'jwb', 'kff', 'mhh', 'nfn', 'njd', 'nkn', 'nsm', 'pgq', 'pjw', 'ppm', 'pst', 'qkn', 'qpb', 'rsg', 'rtf', 'stg', 'tkv', 'vpc', 'wbm', 'wkn', 'wmj', 'wqq', 'wwj']

    # original = definitions.copy()

    # for c, d in itertools.combinations(options, 2):
    #   with open('help5.txt', 'w') as f:

    #     definitions = original.copy()
    rename_history = {}

    #     temp = definitions[c]
    #     definitions[c] = definitions[d]
    #     definitions[d] = temp

    for k in list(definitions.keys()):
      a, op, b = definitions[k]
      if not k.startswith('z') and a[1:].isnumeric() and a[1:] == b[1:]:
        new_key = op[0] + a[1:]
        print('Replacing {} {}'.format(k, new_key))
        rename_history[new_key] = k
        rename_key(definitions, states, k, new_key)

    while True:
      succeeded = False
      for k in list(definitions.keys()):
        new_key = is_B_pair(definitions, k)
        if new_key:
          # print('{} {} {} -> {}'.format(definitions[k][0], definitions[k][1], definitions[k][2], k))
          # a, op, b = definitions[k]
          # new_key = ''
          # if op == 'XOR':
          #   new_key = 'u' + min(a[1:], b[1:])
          # elif op == 'AND':
          #   new_key = 'B' + min(a[1:], b[1:])
          # elif op == 'OR':
          #   new_key = 'C' + min(a[1:], b[1:])
          # else:
          #   assert False

          if k == new_key:
            continue
          print('Replacing {} {}'.format(k, new_key))
          rename_history[new_key] = k
          rename_key(definitions, states, k, new_key)


          succeeded = True
          break
      
      if not succeeded:
        break

    for k in sorted(states.keys()):
      print('{}: {}'.format(k, states[k]))
    print('')
    for k in sorted(definitions.keys()):
      # childs = definitions[k][0], definitions[k][2]
      A, B = sorted([definitions[k][0], definitions[k][2]])
      print('{} {} {} -> {}'.format(A, definitions[k][1], B, k))
      #   # for cmd in data:
      #   #   pass
      # print(c, d)
      # input()

if __name__ == '__main__':
  test('p1 s1', 2024, main(readFileName('s2.txt'), 1))
  # test('p1 real', 45923082839246, main(readFileName('r.txt'), 1))
  # test('p1 real', 45923082839246, main(readFileName('help.txt'), 1))
  # test('p2 s1', 0, main(readFileName('s.txt'), 2))
  test('p2 real', 0, main(readFileName('r.txt'), 2))
