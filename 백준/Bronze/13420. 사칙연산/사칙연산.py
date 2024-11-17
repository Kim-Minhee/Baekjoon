for _ in range(int(input())):
  # 입력
  C = list(input().split())

  # 풀이
  a, b, c = int(C[0]), int(C[2]), int(C[4])
  if C[1]=='+': r = a+b==c
  elif C[1]=='-': r = a-b==c
  elif C[1]=='*': r = a*b==c
  else: r = a//b==c

  # 출력7 - 9 = -2
  if r: print('correct')
  else: print('wrong answer')