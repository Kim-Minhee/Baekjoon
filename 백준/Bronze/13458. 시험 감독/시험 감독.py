# 입력
N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

# 풀이
r = N
A = list(map(lambda a: a-B, A))
for a in A:
  if a>0:
    r += a//C
    if a%C!=0: r += 1

# 출력
print(r)