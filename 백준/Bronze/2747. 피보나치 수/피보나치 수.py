# 함수
def fibo(lst):
  lst.append(lst[-1]+lst[-2])
  return lst

# 입력
N = int(input())

# 풀이
f = [0, 1]
if N>=2:
  while 1:
    f = fibo(f)
    if len(f)==N+1:
      break

# 출력
print(f[-1])