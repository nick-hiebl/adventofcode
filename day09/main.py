import utils as u

lines = u.readFile()

total = 0

highestorder = 0

for line in lines:
  nums = [int(x) for x in line.split(' ')]

  def reduce_data(data):
    out = []
    for i,v in enumerate(data[:-1]):
      out.append(data[i+1] - data[i])
    return out
  
  x = []
  x.append(reduce_data(nums))
  # print(x)
  while not all(z == 0 for z in x[-1]):
    x.append(reduce_data(x[-1]))
  highestorder = max(highestorder, len(x))

  future = sum(z[-1] for z in x) + nums[-1]

  ls = x[::-1] + [nums]
  prev = 0
  for v in ls:
    prev = v[0] - prev

  # print(prev)
  
  total += prev
print(highestorder)
print(total)
