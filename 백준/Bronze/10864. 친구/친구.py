# 입력
N, M = map(int, input().split())

# 풀이
f = [0]*N
for _ in range(M):
  A, B = map(int, input().split())
  f[A-1] += 1
  f[B-1] += 1

# 출력
for i in f:
  print(i)