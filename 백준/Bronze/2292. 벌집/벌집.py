# 입력
N = int(input())

# 풀이
i, a = 1, 1

while a<N:
  a += 6*i
  i += 1

# 출력
print(i)