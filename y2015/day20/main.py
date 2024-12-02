import utils as u

target = 34000000

# most = 10000

def items_at(house):
  presents = 0
  for i in range(1, int(house ** 0.5) + 1):
    if house % i == 0:
      presents += i * 10
      if i * i != house:
        presents += (house // i) * 10

  return presents

def items_at_2(house):
  presents = 0
  for i in range(1, 51):
    if house // i == house / i:
      presents += (house // i) * 11
  return presents

most = -1

i = 1
while True:
  p = items_at_2(i)
  if p >= target:
    print('Found:', i, p)
    break

  if p > most:
    print('Better than last:', i, p)
    most = p

  i += 1
