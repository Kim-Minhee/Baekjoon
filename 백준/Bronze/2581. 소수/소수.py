# 입력
M, N = int(input()), int(input())

# 풀이
num = [1]*10001
num[0], num[1] = 0, 0
for i in range(2, 10001):
  if num[i]:
    for j in range(i*2, 10001, i):
      if num[j]:
        num[j] = 0

prime = list()
for i in range(M, N+1):
  if num[i]:
    prime.append(i)

# 출력
if len(prime)!=0:
  print(sum(prime))
  print(prime[0])
else:
  print(-1)