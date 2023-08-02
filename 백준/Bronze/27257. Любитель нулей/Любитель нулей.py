k = input()
while True:
  if k[0]=='0':
    k = k[1:]
  elif k[-1]=='0':
    k = k[:-1]
  else:
    break
print(k.count('0'))