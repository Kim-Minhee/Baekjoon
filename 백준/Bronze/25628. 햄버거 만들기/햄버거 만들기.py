a, b = map(int, input().split())
h = 0
while a>=2 and b>=1:
  h += 1
  a -= 2
  b -= 1
print(h)