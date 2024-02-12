n = int(input())
xy = list()
for _ in range(n):
  xy.append(list(map(int, input().split())))
res = 0
for i in range(n-1):
  res += abs(xy[i+1][0]-xy[i][0])
  res += abs(xy[i+1][1]-xy[i][1])
res += abs(xy[-1][0]-xy[0][0])
res += abs(xy[-1][1]-xy[0][1])
print(res)