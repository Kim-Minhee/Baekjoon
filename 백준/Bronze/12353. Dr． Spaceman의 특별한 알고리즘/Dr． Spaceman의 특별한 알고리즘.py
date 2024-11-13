import math

for i in range(int(input())):
  # 입력
  C, M, F = map(str, input().split())

  # 풀이
  m = int(M.split('\'')[0])*12+int(M.split('\'')[1][:-1])
  f = int(F.split('\'')[0])*12+int(F.split('\'')[1][:-1])
  c = m+f-5
  if C=='B': c += 10
  c /= 2

  d = 4
  if c!=int(c): d = 3.5
  min_ft = int((c-d)//12)
  max_ft = int((c+d)//12)
  min_ic = int((c-d)%12)
  max_ic = int((c+d)%12)
  
  # 출력
  print(f'Case #{i+1}: {min_ft}\'{min_ic}" to {max_ft}\'{max_ic}"')