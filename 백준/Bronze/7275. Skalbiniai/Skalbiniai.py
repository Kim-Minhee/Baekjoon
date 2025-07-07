N, K, M = map(int, input().split())

num_by_group = []
for _ in range(K):
  num_by_group.append(list(map(int, input().split())))

cnt_by_group = [0]*K
D = list(map(int, input().split()))
for idx, num in enumerate(num_by_group):
  for n in num[1:]:
    cnt_by_group[idx] += D[n-1]

r = 0
for cnt in cnt_by_group:
  r += cnt//M
  if cnt%M>0:
    r += 1
print(r)