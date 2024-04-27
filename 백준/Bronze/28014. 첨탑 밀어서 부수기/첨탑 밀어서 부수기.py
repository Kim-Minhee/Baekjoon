N = int(input())
H = list(map(int, input().split()))
cnt, h = 1, H[0]
for i in range(1, N):
  if h<=H[i]:
    cnt += 1
  h = H[i]
print(cnt)