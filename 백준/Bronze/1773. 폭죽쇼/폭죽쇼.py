# 입력
N, C = map(int, input().split())

# 풀이
f = [False]*(C+1)
r = 0
for _ in range(N):
  # 입력
  t = int(input())
  if t==1:
    r = C
  else:
    for i in range(t, C+1, t):
      if not f[i]:
        f[i] = True
        r += 1

# 출력
print(r)