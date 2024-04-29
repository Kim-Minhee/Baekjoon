N = int(input())
A = list(map(int, input().split()))
m = 0
for i in range(N):
  a = A[i]-N+i
  if m<a:
    m = a
print(m)