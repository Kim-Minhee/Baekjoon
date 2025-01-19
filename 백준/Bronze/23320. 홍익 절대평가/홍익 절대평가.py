N = int(input())
A = list(map(int, input().split()))
X, Y = map(int, input().split())

A.sort()

x = 0.01*X*N
s = len(A[:int(x)])

j = 0
for i, a in enumerate(A):
  if a>=Y:
    j = len(A[i:])
    break

print(s, j)