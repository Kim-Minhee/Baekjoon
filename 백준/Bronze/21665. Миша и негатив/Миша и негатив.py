n, m = map(int, input().split())
ori, w = [], 0
for i in range(n):
  p = input()
  ori.append(p)
input()
for i in range(n):
  p = input()
  for j in range(m):
    if ori[i][j]==p[j]:
      w += 1
print(w)