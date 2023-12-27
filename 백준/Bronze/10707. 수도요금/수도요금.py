a, b, c, d, p = int(input()), int(input()), int(input()), int(input()), int(input())
x, y = p*a, b
if p>c:
  y += (p-c)*d
print(min(x, y))