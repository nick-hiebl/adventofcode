from itertools import groupby

x = '1113122113'

def process2(x):
  # print(list(groupby(x, lambda x: x)))
  s = ''
  for c,n in groupby(x):
    # print(c, len(list(n)))
    s += str(len(list(n))) + str(c)
  return s

def process(x):
  s = ''
  while x:
    first = x[0]
    i = 1
    while i < len(x):
      if x[i] != first:
        break
      i += 1
    s += str(i) + first
    x = x[i:]
  return s

print(process2('11'))

for i in range(50):
  print(i, len(x))
  x = process2(x)

print(len(x))
