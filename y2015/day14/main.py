from utils import *
import re

def processInput(data):
  out = []
  for line in data:
    words = line.split(' ')
    out.append((words[0], int(words[3]), int(words[6]), int(words[13])))
  return out

def simulate(det, dur):
  name, speed, runFor, sleep = det
  dist = 0
  t = 0
  while t + runFor + sleep < dur:
    dist += speed * runFor
    t += runFor + sleep
  dist += min(dur - t, runFor) * speed
  return dist

def main(raw, part):
  total = 0

  data = processInput(raw)

  best = 0

  if part == 1:
    best = max(simulate(x, 2503) for x in data)
    return best
    
  elif part == 2:
    t = 0
    s = { d[0]: { 'dist': 0, 'stars': 0, 'cycle': (0, True) } for d in data }
    while t < 2503:
      for d in data:
        name, speed, runFor, sleep = d
        curr = s[name]
        n,running = curr['cycle']
        if running:
          curr['dist'] += speed
        n += 1
        if running and n == runFor:
          curr['cycle'] = (0, False)
        elif not running and n == sleep:
          curr['cycle'] = (0, True)
        else:
          curr['cycle'] = (n, running)
      
      furthest = max(x['dist'] for x in s.values())
      for d in data:
        name = d[0]
        if s[name]['dist'] == furthest:
          s[name]['stars'] += 1

      t += 1
    return max(x['stars'] for x in s.values())

if __name__ == '__main__':
  part1_sample = main(readFileName('s.txt'), 1)
  print('Part 1 (sample):', part1_sample)
  assert part1_sample == 2660

  part1_real = main(readFileName('r.txt'), 1)
  print('Part 1 (real):', part1_real)
  assert part1_real == 2640

  part2_sample = main(readFileName('s.txt'), 2)
  print('Part 2 (sample):', part2_sample)
  assert part2_sample == 1564

  part2_real = main(readFileName('r.txt'), 2)
  print('Part 2 (real):', part2_real)
  # assert part2_real == 0
