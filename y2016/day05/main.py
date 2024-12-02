from utils import *
import re
import hashlib

def md5(s):
  return hashlib.md5(s.encode('utf-8')).hexdigest()

def processInput(data):
  return data[0].strip()

def main(raw, part):
  total = 0

  data = processInput(raw)

  if part == 1:
    password = ''
    i = 0
    while True:
      res = md5(data + str(i))
      if res.startswith('00000'):
        password += res[5]
        if len(password) == 8:
          return password
      i += 1
  elif part == 2:
    password = ['_'] * 8
    i = 0
    while True:
      res = md5(data + str(i))
      if res.startswith('00000'):
        pos = res[5]
        if pos in '01234567':
          index = int(pos)
          if password[index] == '_':
            password[index] = res[6]
            print(''.join(password))
        if '_' not in password:
          return ''.join(password)
      i += 1

if __name__ == '__main__':
  # part1_sample = main(readFileName('s.txt'), 1)
  # print('Part 1 (sample):', part1_sample)
  # assert part1_sample == '18f47a30'

  # part1_real = main(readFileName('r.txt'), 1)
  # print('Part 1 (real):', part1_real)
  # assert part1_real == 'f77a0e6e'

  # part2_sample = main(readFileName('s.txt'), 2)
  # print('Part 2 (sample):', part2_sample)
  # assert part2_sample == '05ace8e3'

  part2_real = main(readFileName('r.txt'), 2)
  print('Part 2 (real):', part2_real)
  # assert part2_real == 0
