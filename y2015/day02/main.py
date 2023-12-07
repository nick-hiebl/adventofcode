import utils as u

lines = u.readFile()

t = 0
r = 0

for line in lines:
  a,b,c = [int(x) for x in line.strip().split('x')]
  t += 2*(a*b + a*c + b*c)  + min(a*b, a*c, b*c)
  r += 2 * min(a+b,a+c,b+c) + a*b*c

print(t)
print(r)