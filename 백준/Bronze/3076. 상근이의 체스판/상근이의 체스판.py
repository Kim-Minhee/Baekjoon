# 입력
R, C = map(int, input().split())
A, B = map(int, input().split())

# 풀이
chess = []
for i in range(R):
  if i%2==0:
    c = 'X'*B
    for j in range(1, C):
      if j%2==1:
        c += '.'*B
      else:
        c += 'X'*B
  else:
    c = '.'*B
    for j in range(1, C):
      if j%2==1:
        c += 'X'*B
      else:
        c += '.'*B
  for _ in range(A):
    chess.append(c)

# 출력
for c in chess:
  print(c)