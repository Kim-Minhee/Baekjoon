# 입력
h = list()
for _ in range(9):
  h.append(int(input()))

# 풀이 -> 2진수 이용해서 풀면 될듯?!
chk = False
for i in range(0, 8):
  for j in range(i+1, 9):
    check = [1]*9
    check[i], check[j] = 0, 0

    num = 0
    for k in range(9):
      if check[k]:
        num += h[k]

    if num==100:
      chk = True
      break
  if chk:
    break

# 출력
for k in range(9):
  if check[k]:
    print(h[k])