N, M = map(int, input().split())
B = list(map(int, input().split()))
C = []
for _ in range(N):
  C.append(list(map(int, input().split())))

c = 0
for i in range(M-1):
  bi, bo = B[i], B[i+1]
  c += C[bi-1][bo-1]
print(c)