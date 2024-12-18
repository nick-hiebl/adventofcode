from utils import *
import re

def processInput(data):
  regs = {}
  program = []

  for line in data:
    if 'Register' in line:
      regs[line[9]] = int(line[12:])
    if 'Program' in line:
      program = list(map(int, line[9:].split(',')))

  return regs, [(a,b) for a,b in zip(program[::2], program[1::2])]

def read_combo(operand, registers):
  if operand <= 3:
    return operand
  if operand == 4:
    return registers['A']
  elif operand == 5:
    return registers['B']
  else:
    return registers['C']

OUTPUT = []

def do_operation(opcode, operand, registers, pointer):
  global OUTPUT
  if opcode == 0:
    # adv
    registers['A'] //= 2 ** read_combo(operand, registers)
    return pointer + 1
  elif opcode == 1:
    # bxl
    # Should be literal
    # print('Processing opcode', (opcode, operand))
    # assert operand <= 3
    registers['B'] ^= operand
    return pointer + 1
  elif opcode == 2:
    # bst
    registers['B'] = read_combo(operand, registers) % 8
    return pointer + 1
  elif opcode == 3:
    # jnz
    if registers['A'] == 0:
      return pointer + 1
    assert operand <= 3
    return operand
  elif opcode == 4:
    # bxc
    registers['B'] = registers['B'] ^ registers['C']
    return pointer + 1
  elif opcode == 5:
    # out
    OUTPUT.append(read_combo(operand, registers) % 8)
    return pointer + 1
  elif opcode == 6:
    # bdv
    registers['B'] = registers['A'] // (2 ** read_combo(operand, registers))
    return pointer + 1
  elif opcode == 7:
    # cdv
    registers['C'] = registers['A'] // (2 ** read_combo(operand, registers))
    return pointer + 1

def main(raw, part):
  total = 0

  regs, program = processInput(raw)

  global OUTPUT
  OUTPUT = []

  if part == 1:
    # print(regs, program)
    i = 0
    while i < len(program):
      opcode, operand = program[i]
      i = do_operation(opcode, operand, regs, i)
    res = (','.join(str(x) for x in OUTPUT))
      
    return res
  elif part == 2:
    record = 0
    a_start = 0
    while True:
      OUTPUT = []
      regs = { 'A': a_start, 'B': 0, 'C': 0 }

      raw_program = []
      for a,b in program:
        raw_program += [a,b]
      i = 0
      working = True
      while working and i < len(program):
        opcode, operand = program[i]
        i = do_operation(opcode, operand, regs, i)
        if len(OUTPUT) > 0:
          if OUTPUT[len(OUTPUT) - 1] != raw_program[len(OUTPUT) - 1]:
            if len(OUTPUT) > record:
              record = len(OUTPUT) - 1
              print('{0:b}'.format(a_start), record)
            working = False
            break

      if working and all(a == b for a,b in zip(OUTPUT, raw_program)) and len(OUTPUT) == len(raw_program):
        return a_start

      a_start += 1
      # if a_start % 1000 == 0:
      #   print(a_start)

if __name__ == '__main__':
  test('p1 s1', '4,6,3,5,6,3,5,2,1,0', main(readFileName('s.txt'), 1))
  test('p1 real', '1,6,7,4,3,0,5,0,6', main(readFileName('r.txt'), 1))

  # For me, part 2 required a pretty specific hand-rolled un-parsing of the
  # code given in my input. As a result it includes details of my real input,
  # so I can't really check it in.

  # test('p2 s1', 117440, main(readFileName('s2.txt'), 2))
  # test('p2 real', 0, main(readFileName('r.txt'), 2))
