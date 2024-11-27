# 입력
N = list(map(int, input().split()))

# 풀이
if N==sorted(N):
  print('Good')
else:
  print('Bad')