N, M = map(int, input().split())
A = list(map(int, input().split()))

r = -1
s = 0
for i, a in enumerate(A[::-1]):
  s += a
  if s>=M:
    r = N-i
    break

print(r)