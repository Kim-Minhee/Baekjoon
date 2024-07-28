T = int(input())
for _ in range(T):
  # 입력
  R, S = map(str, input().split())

  # 풀이
  r, p = int(R), ''
  for s in S:
    p += s*r

  # 출력
  print(p)