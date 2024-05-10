N = int(input())
D, C = list(), list()
for i in range(N):
  Di, Ci = map(str, input().split())
  D.append(Di)
  C.append(int(Ci))

r, cnt = D.index('jinju'), 0
for j in range(N):
  if C[j]>C[r]:
    cnt += 1
print(C[r])
print(cnt)