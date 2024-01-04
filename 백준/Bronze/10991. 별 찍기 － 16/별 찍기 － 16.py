n = int(input())
for i in range(1, n+1):
  s = ' '*(n-i)
  for _ in range(i-1):
    s += '* '
  s += '*'
  print(s)