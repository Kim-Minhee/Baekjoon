for _ in range(int(input())):
  # 입력
  S = input()
  
  # 풀이
  score = 0
  for s in S:
    if s!=' ':
      score += ord(s)-64

  # 출력
  if score==100: print('PERFECT LIFE')
  else: print(score)