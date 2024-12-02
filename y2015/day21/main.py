from itertools import combinations
from functools import reduce
import utils as u

# boss = { 'hp': 12, 'dmg': 7, 'arm': 2 }
boss = { 'hp': 109, 'dmg': 8, 'arm': 2 }
boss_tup = (boss['hp'], boss['dmg'], boss['arm'])

items = '''
Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3'''

item_list = { 'Weapons': [], 'Armor': [('None', 0, 0, 0)], 'Rings': [] }

key = ''

for line in items.split('\n'):
  if ':' in line:
    key = line.split(':')[0]
    continue
  if not line:
    continue

  ls = [x for x in line.split(' ') if x]

  name, cost, dmg, arm = ' '.join(ls[:-3]), int(ls[-3]), int(ls[-2]), int(ls[-1])
  item_list[key].append((name, cost, dmg, arm))

combos = []

for weapon in item_list['Weapons']:
  for armor in item_list['Armor']:
    combos.append([weapon, armor])

    for ring in item_list['Rings']:
      combos.append([weapon, armor, ring])
    
    for rings in combinations(item_list['Rings'], 2):
      combos.append([weapon, armor, *rings])

price_key = {}

for combo in combos:
  price = sum(map(lambda x: x[1], combo))
  if price not in price_key:
    price_key[price] = []
  reduced = reduce(u.tadd, combo)[1:]

  if reduced == (282, 3, 8):
    print(combo)

  price_key[price].append(reduced)

def simulate(player, boss):
  PRINTING = False

  php, pdmg, parm = player
  bhp, bdmg, barm = boss

  if PRINTING:
    print(player, 'vs.', boss)

  while True:
    bhp -= max(1, pdmg - barm)

    if bhp <= 0:
      return True
    
    if PRINTING: print('Boss down to', bhp, 'after dealing', max(1, pdmg - barm))

    php -= max(1, bdmg - parm)

    if php <= 0:
      return False
    
    if PRINTING: print('Player down to', php, 'after dealing', max(1, bdmg - parm))

# simulate((8, 5, 5), (12, 7, 2))

prices = sorted(price_key.keys())

def part1():
  done = False

  for price in prices:
    for c in price_key[price]:
      if simulate((100, c[1], c[2]), boss_tup):
        print(c)
        done = True
        break
    if done:
      break

def part2():
  done = False

  for price in prices[::-1]:
    for c in price_key[price]:
      if not simulate((100, c[1], c[2]), boss_tup):
        print(c)
        done = True
        break
    if done:
      break

# simulate((100, 3, 8), boss_tup)

part1()
part2()
