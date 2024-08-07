# 함수
def score(x, y):
  d = (x*x+y*y)**(1/2)
  s = 0
  if d<=3:
    s += 100
  elif d<=6:
    s += 80
  elif d<=9:
    s += 60
  elif d<=12:
    s += 40
  elif d<=15:
    s += 20
  return s

# 입력
for _ in range(int(input())):
  P = list(map(float, input().split()))

  # 풀이
  n, m = 0, 0
  for i in range(0, 6, 2):
    n += score(P[i], P[i+1])
  for i in range(6, 12, 2):
    m += score(P[i], P[i+1])

  p = 0
  if n>m:
    p = 1
  elif n<m:
    p = 2

  # 출력
  if p==1 or p==2:
    print(f'SCORE: {n} to {m}, PLAYER {p} WINS.')
  else:
    print(f'SCORE: {n} to {m}, TIE.')