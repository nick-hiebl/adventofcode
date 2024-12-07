from utils import *
import re

def processInput(data):
  out = []

  for line in data:
    target, nums = line.split(': ')
    out.append((int(target), list(map(int, nums.split(' ')))))

  return out

def can_reach_target(target, nums, part=1):
  if nums[0] > target:
    return False
  
  if len(nums) == 1:
    return nums[0] == target
  
  return can_reach_target(target, [nums[0] * nums[1]] + nums[2:], part) \
    or can_reach_target(target, [nums[0] + nums[1]] + nums[2:], part) \
    or (part == 2 and can_reach_target(target, [int(str(nums[0]) + str(nums[1]))] + nums[2:], part))

def main(raw, part):
  total = 0

  data = processInput(raw)

  for target, nums in data:
    if can_reach_target(target, nums, part):
      total += target
  return total

if __name__ == '__main__':
  part1_sample = main(readFileName('s.txt'), 1)
  print('Part 1 (sample):', part1_sample)
  assert part1_sample == 3749

  part1_real = main(readFileName('r.txt'), 1)
  print('Part 1 (real):', part1_real)
  assert part1_real == 21572148763543

  part2_sample = main(readFileName('s.txt'), 2)
  print('Part 2 (sample):', part2_sample)
  assert part2_sample == 11387

  part2_real = main(readFileName('r.txt'), 2)
  print('Part 2 (real):', part2_real)
  assert part2_real == 581941094529163
