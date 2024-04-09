N, S = int(input()), input()
cnt = 0
for i in range(N//2):
  if S[i]!=S[-(i+1)]:
    cnt += 1
print(cnt)