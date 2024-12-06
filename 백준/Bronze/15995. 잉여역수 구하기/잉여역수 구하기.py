# 입력
A, M = map(int, input().split())

# 풀이
i = 1
while 1:
  if (A*i)%M==1:
    print(i)
    break
  i += 1