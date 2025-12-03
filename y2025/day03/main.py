from utils import *
import re
from functools import cache

def processInput(data):
  out = []

  for line in data:
    out.append(tuple(map(int, list(line))))

  return out

my_map = {}

def best_bank_score(key, bank, num_to_choose_from, prior):
  # print('called with', bank, num_to_choose_from, prior)
  if num_to_choose_from == 0:
    return prior
  elif num_to_choose_from > len(bank):
    return 0

  my_key = (key, num_to_choose_from)

  if my_key in my_map:
    if prior < my_map[my_key]:
      return 0

  my_map[my_key] = prior

  a = best_bank_score(key, bank[1:], num_to_choose_from, prior)
  b = best_bank_score(key, bank[1:], num_to_choose_from - 1, prior * 10 + bank[0])

  return max(a,b)

def best_bank_score2(bank, length):
  if length == 0:
    return 0

  first_digit = max(bank[0:len(bank) - length + 1])
  base = first_digit * (10 ** (length - 1))
  return base + best_bank_score2(bank[bank.index(first_digit) + 1:], length - 1)


def main(raw, part):
  total = 0

  data = processInput(raw)

  if part == 1:
    for bank in data:
      v = best_bank_score2(bank, 2)
      total += v
      # best = 0
      # for i, left in enumerate(bank):
      #   if i == len(bank) - 1:
      #     continue
      #   for right in bank[i+1:]:
      #     best = max(best, 10 * left + right)
      
      # total += best
    return total
  elif part == 2:
    global my_map
    for key, bank in enumerate(data):
      v = best_bank_score2(bank, 12)
      # print(v)
      total += v
      # v = best_bank_score(key, bank, 12, 0)
      # print(v)

      # if v == 0:
      #   print(my_map)

      # total += v
      # my_map = {}

    return total

if __name__ == '__main__':
  test('p1 s1', 357, main(readFileName('s.txt'), 1))
  test('p1 real', 17034, main(readFileName('r.txt'), 1))
  test('p2 s1', 3121910778619, main(readFileName('s.txt'), 2))
  test('p2 real', 168798209663590, main(readFileName('r.txt'), 2))
