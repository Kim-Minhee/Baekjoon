# 함수
def cal(num, opr):
  if opr=='@':
    return num*3
  elif opr=='%':
    return num+5
  elif opr=='#':
    return num-7

for _ in range(int(input())):
  # 입력
  L = list(map(str, input().split()))

  # 풀이
  num = float(L[0])
  for opr in L[1:]:
    num = cal(num, opr)

  # 출력
  print(f'{num:.2f}')