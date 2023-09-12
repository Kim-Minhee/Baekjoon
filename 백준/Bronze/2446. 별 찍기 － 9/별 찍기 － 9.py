n = int(input())
star = list()
for i in range(n):
  s = ' '*i
  s += '*'*(2*(n-i)-1)
  star.append(s)
  print(s)
for i in range(n-1, 0, -1):
  print(star[i-1])