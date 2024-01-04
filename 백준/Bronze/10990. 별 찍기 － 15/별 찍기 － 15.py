n = int(input())
for i in range(1, n+1):
  s = ' '*(n-i)
  s += '*'
  if i!=1:
    s += ' '*(2*i-3)
    s += '*'
  print(s)