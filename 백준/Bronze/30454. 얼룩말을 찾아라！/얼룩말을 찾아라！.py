N, L = map(int, input().split())
h = list()
for _ in range(N):
  H, l = input(), 0
  for i in range(L):
    if H[i]=='1':
        l += 1
        if i!=0 and H[i-1]=='1':
            l -= 1
  h.append(l)
m = max(h)
cnt = h.count(m)
print(m, cnt)