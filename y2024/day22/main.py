from utils import *
import re

def processInput(data):
  out = []

  for line in data:
    out.append(int(line))

  return out

def mix(value, secret):
  return value ^ secret

def prune(secret):
  return secret % 16777216

def next_secret(secret):
  secret = prune(mix(secret, secret * 64))
  secret = prune(mix(secret, secret // 32))
  secret = prune(mix(secret, secret * 2048))
  return secret

def repeat_times(start, n):
  for i in range(n):
    start = next_secret(start)

  return start

def produce_sequence(start, steps):
  nums = [start]
  for i in range(2000):
    start = next_secret(start)
    nums.append(start)
  
  return [n % 10 for n in nums]

def produce_priors(sequence):
  best_to_get = {}

  for i in range(0, len(sequence) - 4):
    cs = sequence[i:i+5]
    assert len(cs) == 5
    key = tuple(b-a for a,b in zip(cs, cs[1:]))

    if key not in best_to_get:
      best_to_get[key] = cs[-1]
  
  return best_to_get

def main(raw, part):
  total = 0

  data = processInput(raw)

  if part == 1:
    for s in data:
      total += repeat_times(s, 2000)
    return total
  elif part == 2:
    all_keys = defaultdict(int)

    for trader in data:
      seq = produce_sequence(trader, 2000)
      priors = produce_priors(seq)

      for k in priors.keys():
        all_keys[k] += priors[k]
    
    return max(all_keys.values())

    return total

if __name__ == '__main__':
  test('p1 s1', 37327623, main(readFileName('s.txt'), 1))
  test('p1 real', 14622549304, main(readFileName('r.txt'), 1))
  test('p2 s1', 23, main(readFileName('s2.txt'), 2))
  test('p2 real', 0, main(readFileName('r.txt'), 2))
