# Part 1
import utils as u

lines = u.readFile()

cards = list('AKQJT98765432')

data = []

def rank(hand):
  vals = list(set(hand))
  counts = set(hand.count(v) for v in vals)
  raws = list(hand.count(v) for v in vals)
  if counts == {5}:
    return '9 -5okind'
  elif counts == {4,1}:
    return '8 -4okind'
  elif counts == {3,2}:
    return '7 -fulhouse'
  elif counts == {3,1}:
    return '6 -3okind'
  elif raws.count(2) == 2:
    return '5 -2pair'
  elif raws.count(2) == 1:
    return '4 -1pair'
  else:
    return '2 -highcard'

for line in lines:
  raw_hand,b = line.split(' ')
  bid = int(b)
  hand = tuple(cards.index(c) for c in raw_hand)
  data.append((hand, bid, raw_hand))

data.sort(key=lambda x: (rank(x[0]), tuple(-z for z in x[0])))

total = 0
for rank, d in enumerate(data):
  total += (rank + 1) * d[1]

print(data)
print('total:', total)

