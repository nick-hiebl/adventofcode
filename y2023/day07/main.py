# Part 2
import utils as u

lines = u.readFile()

cards = list('AKQT98765432J')
jINDEX = cards.index('J')

data = []

def rank(hand):
  jokers = list(hand).count(jINDEX)
  vals = list(set(c for c in hand if c != jINDEX))
  counts = set(hand.count(v) for v in vals)
  raws = list(hand.count(v) for v in vals)
  if 5 in counts or jokers == 5 or max(counts) + jokers == 5:
    return '9 -5okind'
  elif 4 in counts or max(counts) + jokers == 4:
    return '8 -4okind'
  elif counts == {3,2} or (counts == {2,2} and jokers == 1):
    return '7 -fulhouse'
  elif 3 in counts or max(counts) + jokers == 3:
    return '6 -3okind'
  elif raws.count(2) == 2:
    return '5 -2pair'
  elif raws.count(2) == 1 or max(counts) + jokers == 2:
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

print(' '.join(d[2] for d in data))
print('total:', total)

