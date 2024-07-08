for _ in range(int(input())):
  # 입력
  N = int(input())

  # 풀이
  n = str(N**2)[-len(str(N)):]

  # 출력
  if str(N)==n:
    print('YES')
  else:
    print('NO')