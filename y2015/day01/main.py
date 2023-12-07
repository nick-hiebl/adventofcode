import utils as u

lines = u.readFile()

l = lines[0]
i = 0
for index,c in enumerate(l):
  if c == '(':
    i += 1
  else:
    i -= 1
  
  if i == -1:
    print(index + 1)

print(l.count('(') - l.count(')'))
