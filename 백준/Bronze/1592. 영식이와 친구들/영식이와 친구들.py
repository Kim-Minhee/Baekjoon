# 입력
N, M, L = map(int, input().split())

# 풀이
p = {1:1}
for i in range(2, N+1):
  p[i] = 0
ball, cnt = 1, 0
while p[ball]!=M:
  if p[ball]%2==1:
    ball += L%N
    if ball>N:
      ball -= N
  else:
    ball -= L%N
    if ball<=0:
      ball += N
  p[ball] += 1
  cnt += 1

# 출력
print(cnt)