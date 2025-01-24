N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

r = 0
for i in range(min(N, M)):
  if B[i]>A[i] and B[i]-A[i]>r:
    r = B[i]-A[i]
if N<M and r<max(B[N:]):
  r = max(B[N:])

print(r)