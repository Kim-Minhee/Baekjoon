# 입력
A, B, C = int(input()), int(input()), int(input())

# 풀이
num = str(A*B*C)
cnt = [0]*10
for n in num:
  cnt[int(n)] += 1

# 출력
for c in cnt:
  print(c)