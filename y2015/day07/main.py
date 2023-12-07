import utils as u

lines = u.readFile()

Map = {}
value = {}

for line in lines:
  defn, name = line.split(' -> ')
  Map[name] = defn

def compute(name):
  if name in value:
    return value[name]
  if name.isnumeric():

    v = int(name)
    value[name] = v
    return v
  mean = Map[name]

  # print('Computing', name)

  if mean.isnumeric():
    v = int(mean)
    value[name] = v
    return v
  
  ws = mean.split(' ')

  if len(ws) == 1:
    v = compute(ws[0])
    value[name] = v
    return v
  elif len(ws) == 2:
    v = (~compute(ws[1]) & 65535)
    value[name] = v
    return v
  if len(ws) == 3:
    if ws[1] == 'AND':
      v = compute(ws[0]) & compute(ws[2])
      value[name] = v
      return v
    elif ws[1] == 'OR':
      v = compute(ws[0]) | compute(ws[2])
      value[name] = v
      return v
    elif ws[1] == 'LSHIFT':
      v = compute(ws[0]) << compute(ws[2])
      value[name] = v
      return v
    elif ws[1] == 'RSHIFT':
      v = compute(ws[0]) >> compute(ws[2])
      value[name] = v
      return v

for name in Map.keys():
  compute(name)

a_value = (compute('a'))
value = {'b': a_value}
print(compute('a'))
print(value)
