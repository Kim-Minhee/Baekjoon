# 입력
N = input()

# 풀이
n = ''
for i in range(1, 100001):
  n += str(i)

# 출력
print(n.index(N)+1)