n, m = map(int, input().split())
b = [0 for i in range(n)]
for _ in range(m):
  i, j, k = map(int, input().split())
  for b_ in range(i-1, j):
    b[b_] = k
print(*b)