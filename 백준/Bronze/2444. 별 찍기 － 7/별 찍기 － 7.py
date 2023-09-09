n = int(input())
for i in range(1, n+1):
  s = ' '*(n-i)
  s += '*'*(2*i-1)
  print(s)
for i in range(1, n):
  s = ' '*i
  s += '*'*(2*(n-i)-1)
  print(s)