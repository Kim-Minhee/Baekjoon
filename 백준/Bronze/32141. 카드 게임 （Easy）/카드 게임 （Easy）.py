N, H = map(int, input().split())
D = list(map(int, input().split()))

r = -1
for i, d in enumerate(D):
  H -= d
  if H<=0:
    r = i+1
    break

print(r)