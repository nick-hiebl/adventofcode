from utils import *
import itertools

def processInput(data, part):
  out = {}
  for line in data:
    words = line[:-1].split(' ')
    me = words[0]
    them = words[10]
    pos = 1 if words[2] == 'gain' else -1
    num = int(words[3]) * pos
    meSec = out.get(me, { 'Me': 0 })
    out[me] = meSec
    meSec[them] = num
  if part == 2:
    out['Me'] = { o: 0 for o in out.keys() }
  return out

def rateOrder(order, ratings):
  rate = 0
  for a,b in zip(order, order[1:]):
    rate += ratings[a][b] + ratings[b][a]
  rate += ratings[order[0]][order[-1]] + ratings[order[-1]][order[0]]

  return rate

def main(raw, part):
  total = 0

  ratings = processInput(raw, part)
  people = list(ratings.keys())

  if part == 1:
    return max(rateOrder([people[0]] + list(os), ratings) for os in itertools.permutations(people[1:], len(people) - 1))

  elif part == 2:
    return max(rateOrder([people[0]] + list(os), ratings) for os in itertools.permutations(people[1:], len(people) - 1))

if __name__ == '__main__':
  part1_sample = main(readFileName('s.txt'), 1)
  print('Part 1 (sample):', part1_sample)
  assert part1_sample == 330

  part1_real = main(readFileName('r.txt'), 1)
  print('Part 1 (real):', part1_real)
  assert part1_real == 733

  part2_sample = main(readFileName('s.txt'), 2)
  print('Part 2 (sample):', part2_sample)
  # assert part2_sample == 0

  part2_real = main(readFileName('r.txt'), 2)
  print('Part 2 (real):', part2_real)
  # assert part2_real == 0
