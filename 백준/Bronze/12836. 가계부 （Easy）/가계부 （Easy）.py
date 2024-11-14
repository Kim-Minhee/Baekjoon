# 입력
N, Q = map(int, input().split())
money = [0]*(N+1)
for _ in range(Q):
  A, B, C = map(int, input().split())

  # 풀이
  if A==1:
    money[B] += C
  else:
    # 출력
    print(sum(money[B:C+1]))