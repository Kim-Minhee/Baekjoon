N, A = input(), list(input())

bs = ['B', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'V', 'Z']
bs_cnt = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for a in A:
  if a in bs:
    bs_cnt[bs.index(a)] += 1

r = 0
while True:
  chk = [1, 2, 1, 1, 1, 1, 2, 1, 1, 1]
  for i in range(10):
    bs_cnt[i] -= chk[i]

  if -1 not in bs_cnt and -2 not in bs_cnt:
    r += 1
  else: break

print(r)