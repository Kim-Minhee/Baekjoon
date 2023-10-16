x, y, rx, ry = list(), list(), int(), int()
for _ in range(3):
  x_, y_ = map(int, input().split())
  x.append(x_)
  y.append(y_)
x.sort()
if x[0]==x[1]:
  rx = x[2]
else:
  rx = x[0]
y.sort()
if y[0]==y[1]:
  ry = y[2]
else:
  ry = y[0]
print(rx, ry)