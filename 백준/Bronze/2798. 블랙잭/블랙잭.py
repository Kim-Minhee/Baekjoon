# 입력
N, M = map(int, input().split())
C = list(map(int, input().split()))

# 풀이
m = list()
for i in range(N):
  for j in range(i+1, N):
    for k in range(j+1, N):
      if C[i]+C[j]+C[k]<=M:
        m.append(C[i]+C[j]+C[k])
m.sort()

# 출력
print(m[-1])