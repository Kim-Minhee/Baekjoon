N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

r1, r2 = sum(A), 0
for i, b in enumerate(B):
  if b==0:
    r2 += A[i]

print(r1)
print(r2)