# 입력
N = int(input())

# 풀이
time = 0
while N!=0:
  k = 1
  while k<=N:
    N -= k
    k += 1
  time += k-1

# 출력
print(time)