X, S = map(int, input().split())

x, s, j = X, S, 0
while True:
  if x<=0:
    break
  if s<=1:
    j += x
    break
  j += 1
  x -= s
  s = int(s/2)

print(j)