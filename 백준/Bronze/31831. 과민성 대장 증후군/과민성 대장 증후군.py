N, M = map(int, input().split())
S = list(map(int, input().split()))
s, d = 0, 0
for i in S:
  s += i
  if s<0:
    s = 0
  if s>=M:
    d += 1
print(d)