from utils import *

def processInput(data):
  out = []

  for line in data:
    out.append(tuple(map(int, list(line))))

  return out

def best_bank_score(bank, length, prior = 0):
  if length == 0:
    return prior

  first_digit = max(bank[0:len(bank) - length + 1])
  remaining_digits = bank[bank.index(first_digit) + 1:]
  return best_bank_score(remaining_digits, length - 1, prior * 10 + first_digit)

def main(raw, part):
  total = 0

  data = processInput(raw)

  if part == 1:
    for bank in data:
      total += best_bank_score(bank, 2)
    return total
  elif part == 2:
    global my_map
    for key, bank in enumerate(data):
      total += best_bank_score(bank, 12)

    return total

if __name__ == '__main__':
  test('p1 s1', 357, main(readFileName('s.txt'), 1))
  test('p1 real', 17034, main(readFileName('r.txt'), 1))
  test('p2 s1', 3121910778619, main(readFileName('s.txt'), 2))
  test('p2 real', 168798209663590, main(readFileName('r.txt'), 2))
