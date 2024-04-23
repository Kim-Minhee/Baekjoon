N = int(input())
C = list(map(int, input().split()))
g, r = [[C[0]]], 0

for i in range(1, N):
  if C[i]-C[i-1]==1:
    g[-1].append(C[i])
  else:
    g.append([C[i]])

for i in range(len(g)):
  r += g[i][0]
print(r)