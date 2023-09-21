a, b = map(int, input().split())
c = int(input())
a2, b2 = c//60, c%60
h, m = a+a2, b+b2
if m>=60:
  m -= 60
  h += 1
if h>=24:
  h -= 24
print(h, m)