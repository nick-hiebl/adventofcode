import utils as u

lines = u.readFile()

rules = []
start = lines[-1]

for index,line in enumerate(lines):
  if not line:
    break
  
  rules.append(tuple(line.split(' => ')[::-1]))

print(rules)
print(start)

def make_next(priors):
  possibilities = set()

  for prior in priors:
    for search,repl in rules:
      s_len = len(search)
      for i in range(len(prior) - s_len + 1):
        if prior[i:i+s_len] == search:
          possibilities.add(prior[:i] + repl + prior[i+s_len:])
  return possibilities

def make_a_replacement(prior):
  for search,repl in rules:
    s_len = len(search)
    for i in range(len(prior) - s_len + 1):
      if prior[i:i+s_len] == search:
        return prior[:i] + repl + prior[i+s_len:]

i = 0
# current = set()
# current.add(start)
current = start
while True:
  i += 1
  current = make_a_replacement(current)
  # current = set(filter(lambda x: len(x) <= len(start), current))
  # all_letters = sum(map(len, current))
  # print(i, len(current), all_letters, all_letters / len(current))
  # if 'e' in current:
  if current == 'e':
    print('Done:', i)
    break
  print(current)
  # print(current)