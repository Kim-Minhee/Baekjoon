N, M = map(int, input().split())

vote = {}
for m in range(1, M+1):
  vote[m] = 0

for _ in range(N):
  V = list(map(int, input().split()))
  for i, v in enumerate(V):
    if v:
      vote[i+1] += 1

vote_r = {}
for k, v in vote.items():
  if v in vote_r.keys():
    vote_r[v] = vote_r[v] + ' ' + str(k)
  else:
    vote_r[v] = str(k)

vote_num = list(vote_r.keys())
vote_num.sort(reverse=True)
r = ''
for num in vote_num:
  r += vote_r[num]
  r += ' '

print(r[:-1])