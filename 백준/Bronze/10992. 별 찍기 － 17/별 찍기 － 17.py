n = int(input())
for i in range(1, n+1):
  s = ' '*(n-i)
  if i!=n:
    s += '*'
    if i!=1:
      s += ' '*(2*i-3)
      s += '*'
  else:
    s = '*'*(2*i-1)
  print(s)