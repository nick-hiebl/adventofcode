from utils import *

def processInput(data):
  out = []

  for line in data:
    out.append(line.split(' '))

  return out

def main(raw, part):
  total = 0

  data = processInput(raw)

  regs = [0, 0] if part == 1 else [1, 0]

  def reg_index(s):
    return 0 if s[0] == 'a' else 1

  cmd_index = 0
  while True:
    if cmd_index >= len(data):
      break
    cmd = data[cmd_index]
    print(cmd_index, cmd, regs)
    if cmd[0] == 'hlf':
      regs[reg_index(cmd[1])] //= 2
      cmd_index += 1
    elif cmd[0] == 'tpl':
      regs[reg_index(cmd[1])] *= 3
      cmd_index += 1
    elif cmd[0] == 'inc':
      regs[reg_index(cmd[1])] += 1
      cmd_index += 1
    elif cmd[0] == 'jmp':
      cmd_index += int(cmd[1])
    elif cmd[0] == 'jie':
      if regs[reg_index(cmd[1])] % 2 == 0:
        cmd_index += int(cmd[2])
      else:
        cmd_index += 1
    elif cmd[0] == 'jio':
      if regs[reg_index(cmd[1])] == 1:
        cmd_index += int(cmd[2])
      else:
        cmd_index += 1
    else:
      print('Unexpected command', cmd)
      assert cmd[0] == ''
  return regs[1]

if __name__ == '__main__':
  part1_sample = main(readFileName('s.txt'), 1)
  print('Part 1 (sample):', part1_sample)
  assert part1_sample == 0

  part1_real = main(readFileName('r.txt'), 1)
  print('Part 1 (real):', part1_real)
  assert part1_real == 307

  part2_sample = main(readFileName('s.txt'), 2)
  print('Part 2 (sample):', part2_sample)
  assert part2_sample == 0

  part2_real = main(readFileName('r.txt'), 2)
  print('Part 2 (real):', part2_real)
  # assert part2_real == 0
