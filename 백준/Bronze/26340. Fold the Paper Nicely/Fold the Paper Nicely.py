n = int(input())
for i in range(n):
  a, b, c = map(int, input().split())
  print('Data set:', a, b, c)
  for _ in range(c):
    l, s = max(a, b), min(a, b)
    a = l//2
    b = s
  print(max(a, b), min(a, b))
  if i!=(n-1):
    print()