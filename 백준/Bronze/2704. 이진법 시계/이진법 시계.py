# 함수
def changeBin(num):
  r = bin(num)[2:]
  return '0'*(6-len(r))+r

for _ in range(int(input())):
  # 입력
  H, M, S = map(int, input().split(':'))

  # 풀이
  h, m, s = changeBin(H), changeBin(M), changeBin(S)
  r = ''
  for i in range(6):
    r += h[i]+m[i]+s[i]
  c = h+m+s

  # 출력
  print(r, c)