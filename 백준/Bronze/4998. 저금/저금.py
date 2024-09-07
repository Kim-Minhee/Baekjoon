try:
  while 1:
    # 입력
    N, B, M = map(float, input().split())

    # 풀이
    y = 0
    while N<=M:
      y += 1
      N += N*(B/100)

    # 출력
    print(y)
except:
  pass