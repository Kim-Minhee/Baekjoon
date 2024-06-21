N = int(input())
W = list(map(int, input().split()))
s, cnt = [0 for _ in range(100)], 0
for w in W:
  if s[w-1]==0:
    s[w-1] = 1
  else:
    cnt += 1
print(cnt)