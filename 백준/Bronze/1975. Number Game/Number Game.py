import sys

# 입력
T = int(sys.stdin.readline())
for _ in range(T):
  N = int(sys.stdin.readline())

  # 풀이
  cnt = 0
  for i in range(2, N+1):
    n = N
    while 1:
      if n%i==0:
        cnt += 1
        n //= i
      else:
        break

  # 출력
  print(cnt)