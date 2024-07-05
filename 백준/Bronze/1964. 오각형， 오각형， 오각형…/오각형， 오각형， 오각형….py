# 입력
N = int(input())

# 풀이
d = 0
for i in range(1, N+1):
  if i==1:
    d += 5
  else:
    d += i+1
    d += 2*i

# 출력
print(d%45678)