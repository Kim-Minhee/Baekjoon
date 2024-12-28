N, M = map(int, input().split())
X = list(map(int, input().split()))

max_cnt = 0
for i in range(1, M+1):
  cnt = X.count(i)
  if cnt>max_cnt:
    max_cnt = cnt

print(max_cnt)