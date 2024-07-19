for _ in range(3):
  # 입력
  num = input()

  # 풀이
  maxCnt, cnt = 1, 1
  for i in range(1, 8):
    if num[i]==num[i-1]:
      cnt += 1
      if cnt>maxCnt:
        maxCnt = cnt
    else:
      cnt = 1

  # 출력
  print(maxCnt)