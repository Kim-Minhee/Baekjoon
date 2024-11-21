# 입력
T = int(input())

# 풀이
r = ''
while T>0:
  r += str(T%9)
  T //= 9

# 출력
print(r[::-1])