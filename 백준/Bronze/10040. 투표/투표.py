# 입력
N, M = map(int, input().split())
A, B = [], []
for _ in range(N):
  A.append(float(input()))
for _ in range(M):
  B.append(float(input()))

# 풀이
# A.sort(reverse=True)
v = [0]*N
for b in B:
  for i, a in enumerate(A):
    if b>=a:
      v[i] += 1
      break
m = max(v)

# 출력
print(v.index(m)+1)