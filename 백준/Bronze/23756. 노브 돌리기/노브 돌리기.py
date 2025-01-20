N, A0 = int(input()), int(input())

r = 0
for _ in range(N):
  A = int(input())
  if abs(A-A0)<=180:
    r += abs(A-A0)
  else:
    r += 360-abs(A-A0)
  A0 = A

print(r)