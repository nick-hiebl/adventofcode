from utils import *
import re

def processInput(data):
  orders = []
  books = []

  for line in data:
    if '|' in line:
      orders.append(tuple(map(int, line.split('|'))))
    elif ',' in line:
      books.append(tuple(map(int, line.split(','))))

  return orders, books

def is_valid(book, orders):
  for a,b in orders:
    if a in book and b in book:
      if book.index(a) > book.index(b):
        return False
  return True

def reorder(base_book, orders):
  book = list(base_book[:])
  for a,b in orders:
    if a in book and b in book:
      a1, b1 = book.index(a), book.index(b)
      if a1 > b1:
        book[b1] = a
        book[a1] = b
  return book

def main(raw, part):
  total = 0

  orders, books = processInput(raw)

  if part == 1:
    for book in books:
      if is_valid(book, orders):
        total += book[len(book) // 2]
    return total
  elif part == 2:
    for book in books:
      if not is_valid(book, orders):
        print(book)
        b2 = reorder(book, orders)
        while not is_valid(b2, orders):
          b2 = reorder(b2, orders)
        total += b2[len(b2) // 2]
    return total

if __name__ == '__main__':
  part1_sample = main(readFileName('s.txt'), 1)
  print('Part 1 (sample):', part1_sample)
  assert part1_sample == 143

  part1_real = main(readFileName('r.txt'), 1)
  print('Part 1 (real):', part1_real)
  assert part1_real == 5509

  part2_sample = main(readFileName('s.txt'), 2)
  print('Part 2 (sample):', part2_sample)
  assert part2_sample == 123

  part2_real = main(readFileName('r.txt'), 2)
  print('Part 2 (real):', part2_real)
  # assert part2_real == 0
