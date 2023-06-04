n = int(input())
a, b = map(int, input().split())
c = 0
while n>0:
  if a>1:
    n -= 1
    a -= 2
    c += 1
  elif b>0:
    n -= 1
    b -= 1
    c += 1
  else:
    break
print(c)