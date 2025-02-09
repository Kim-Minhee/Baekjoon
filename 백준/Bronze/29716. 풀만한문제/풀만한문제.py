upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
J, N = map(int, input().split())

cnt = 0
for _ in range(N):
  P = input()
  score = 0
  for p in P:
    if p in upper:
      score += 4
    elif p==' ':
      score += 1
    else:
      score += 2
  if score<=J:
    cnt += 1

print(cnt)