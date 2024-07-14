def bun(num):
  b = num
  for n in str(num):
    b += int(n)
  return b

# 입력
N = int(input())

# 풀이
chk = False
for i in range(1, N):
  if bun(i)==N:
    r = i
    chk = True
    break

# 출력
if chk:
  print(r)
else:
  print(0)