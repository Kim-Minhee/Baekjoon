for _ in range(int(input())):
  # 입력
  K, N = map(str, input().split())

  # 풀이
  if '8' in N or '9' in N: o = 0
  else: o = int(N, 8)
  x = int(N, 16)

  # 출력
  print(K, o, int(N), x)