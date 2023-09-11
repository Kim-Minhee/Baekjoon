n = int(input())
for i in range(1, n+1):
  s = '*'*i
  s += ' '*(2*(n-i))
  s += '*'*i
  print(s)
for i in range(n-1, 0, -1):
  s = '*'*i
  s += ' '*(2*(n-i))
  s += '*'*i
  print(s)