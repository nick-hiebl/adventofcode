import utils as u

lines = u.readFile()
# lines = ['""', '"abc"', '"aaa\\"aaa"', '"\\x27"']

real = 0
fake = 0
stupid = 0

for line in lines:
  l = line.strip()
  real += len(eval(l))
  fake += len(l)
  stupid += len(l) + 2 + l.count('"') + l.count('\\')

print(fake - real)
print(stupid - fake)
