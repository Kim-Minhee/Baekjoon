try:
  while 1:
    # 입력
    N, K = map(int, input().split())

    # 풀이
    c = N
    while N>=K:
      n = N//K
      c += n
      N %= K
      N += n

    # 출력
    print(c)
except:
  exit()