# 입력
N = int(input())

# 풀이
fibo = [0, 1, 1]
if N<=2:
  print(fibo[N])
else:
  for i in range(3, N+1):
    fibo.append(fibo[i-2]+fibo[i-1])
  print(fibo[-1])