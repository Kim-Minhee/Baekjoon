# 입력
A, B = map(int, input().split())

# 풀이
a = min(A, B)
b = max(A, B)

# 출력
if a==b:
  print(0)
else:
  print(b-a-1)
  for i in range(a+1, b):
    print(i, end=' ')