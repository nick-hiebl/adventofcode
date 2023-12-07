import hashlib

abc = 'abcdef'
mine = 'yzbqklnj'

i = 0
while True:
  h = hashlib.md5((mine + str(i)).encode('utf-8')).hexdigest()
  if h.startswith('000000'):
    print(i)
    break
  i += 1