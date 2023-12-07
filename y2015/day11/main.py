password = 'cqjxxyzz'
code = list(ord(x) - ord('a') for x in password)
def increment(pwd):
  for j in range(len(pwd) - 1, -1, -1):
    pwd[j] += 1
    if pwd[j] < 26:
      break
    else:
      pwd[j] = 0

increment(code)
alpha = 'abcdefghijklmnopqrstuvwxyz'
while True:
  password = ''.join(chr(x + ord('a')) for x in code)
  if 'i' not in password and 'o' not in password and 'l' not in password:
    if any(alpha[i:i+3] in password for i in range(len(alpha)-2)):
      if sum(int(x+x in password) for x in alpha) >= 2:
        break

  increment(code)

print(password)
