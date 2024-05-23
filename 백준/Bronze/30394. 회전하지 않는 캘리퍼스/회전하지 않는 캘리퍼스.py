N = int(input())
ymax, ymin = int(), int()
for i in range(N):
  X, Y = map(int, input().split())
  if i==0:
    ymax = Y
    ymin = Y
  else:
    if Y>ymax:
      ymax = Y
    if Y<ymin:
      ymin = Y
print(ymax-ymin)