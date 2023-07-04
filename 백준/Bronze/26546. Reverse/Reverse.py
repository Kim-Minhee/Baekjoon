n = int(input())
for _ in range(n):
  m, i, j = map(str, input().split())
  r = m[:int(i)] + m[int(j):]
  print(r)