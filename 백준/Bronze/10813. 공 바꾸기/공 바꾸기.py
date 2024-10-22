# 입력
N, M = map(int, input().split())

# 풀이
ball = [x for x in range(1, N+1)]
for _ in range(M):
  I, J = map(int, input().split())
  ball[I-1], ball[J-1] = ball[J-1], ball[I-1]

# 출력
print(*ball)