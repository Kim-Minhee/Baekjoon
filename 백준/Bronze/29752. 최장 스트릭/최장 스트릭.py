N = int(input())
S = list(map(int, input().split()))
ms, s = 0, 0
for i in range(N):
  if S[i]>0:
    s += 1
    ms = max(ms, s)
  else:
    s = 0
print(ms)