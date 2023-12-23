x_max = y_max = -10001
x_min = y_min = 10001
for _ in range(int(input())):
  x, y = map(int, input().split())
  if x>x_max:
    x_max = x
  if y>y_max:
    y_max = y
  if x<x_min:
    x_min = x
  if y<y_min:
    y_min = y
print((y_max-y_min)*(x_max-x_min))