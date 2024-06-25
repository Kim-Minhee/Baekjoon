# 입력
N, L = map(int, input().split())

# 풀이
n, i = list(), 1
while len(n)!=N:
  if str(L) not in str(i):
    n.append(i)
  i += 1

# 출력
print(n[-1])