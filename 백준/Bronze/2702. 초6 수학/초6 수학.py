import math

T = int(input())
for _ in range(T):
  # 입력
  A, B = map(int, input().split())

  # 풀이
  lcm = math.lcm(A, B)
  gcd = math.gcd(A, B)

  # 출력
  print(lcm, gcd)