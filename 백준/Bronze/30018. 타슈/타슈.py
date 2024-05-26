N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
r = 0
for i in range(N):
  r += abs(A[i]-B[i])
print(r//2)