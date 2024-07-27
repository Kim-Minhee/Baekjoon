# 입력
S = int(input())
N = list(map(int, input().split()))

# 풀이
l = [1]
for s in range(2, S+1):
  l.insert(s-1-N[s-1], s)

# 출력
print(*l)