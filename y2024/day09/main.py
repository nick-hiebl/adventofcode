from utils import *
import re

def processInput(data):
  out = []

  gap = False
  block = 0
  for c in data[0]:
    if gap:
      out += ['.'] * int(c)
    else:
      out += [block] * int(c)
      block += 1
    gap = not gap

  return out

def process2(data):
  out = []
  gaps = []
  gap = False
  block_id = 0
  position = 0
  for c in data[0]:
    if gap:
      gaps.append((position, int(c)))
      position += int(c)
    else:
      out.append((block_id, position, int(c)))
      position += int(c)
      block_id += 1
    gap = not gap

  return out, gaps

def show(data):
  print(''.join(str(c) for c in data))

def chunk(sequence):
  i = 0
  while i < len(sequence) - 1:
    if all(x == '.' for x in sequence[i:]):
      return sequence[:i]
    if sequence[i] != '.':
      i += 1
      continue
    else:
      last = sequence.pop()
      while last == '.' and len(sequence) >= i:
        last = sequence.pop()
      if len(sequence) <= i:
        print(i, len(sequence), sequence[i:])
        assert False
      sequence[i] = last
      i += 1
      # show(sequence)
      continue

  return sequence

def checksum(x):
  return sum(i * (v if type(v) == type(1) else 0) for i,v in enumerate(x))


def checksum2(blocks):
  total = 0
  for block_id, pos, size in blocks:
    for j in range(size):
      total += block_id * (pos + j)
  return total

def chunk2(blocks, gaps):
  i = len(blocks) - 1
  acceptable_id = blocks[-1][0] + 1
  while i > 0:
    block = blocks[i]
    block_id, position, block_size = block
    # Already moved
    if block_id >= acceptable_id:
      i -= 1
      continue
    acceptable_id = min(acceptable_id, block_id)

    j = 0
    possible = True
    while j < len(gaps):
      gap = gaps[j]
      gap_position, gap_size = gap
      if gap_position >= position:
        possible = False
        break
      if gap_size < block_size:
        j += 1
        continue
      break
    if j == len(gaps):
      possible = False
    # Nowhere to put it
    if not possible:
      i -= 1
      continue
    if block_size == gap_size:
      gaps.pop(j)
      blocks[i] = (block_id, gap_position, block_size)
    elif block_size < gap_size:
      gaps[j] = (gap_position + block_size, gap_size - block_size)
      blocks[i] = (block_id, gap_position, block_size)

    i -= 1
  return blocks, gaps



def main(raw, part):
  total = 0

  if part == 1:
    data = processInput(raw)
    chunk(data)
    return checksum(data)
  elif part == 2:
    blocks, gaps = process2(raw)

    chunk2(blocks, gaps)

    return checksum2(blocks)

if __name__ == '__main__':
  part1_sample = main(readFileName('s.txt'), 1)
  print('Part 1 (sample):', part1_sample)
  assert part1_sample == 1928

  part1_real = main(readFileName('r.txt'), 1)
  print('Part 1 (real):', part1_real)
  assert part1_real == 6154342787400

  part2_sample = main(readFileName('s.txt'), 2)
  print('Part 2 (sample):', part2_sample)
  assert part2_sample == 2858

  part2_real = main(readFileName('r.txt'), 2)
  print('Part 2 (real):', part2_real)
  assert part2_real == 6183632723350
