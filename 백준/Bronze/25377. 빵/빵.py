n = int(input())
r = 1001
for _ in range(n):
  a, b = map(int, input().split())
  if a<=b:
    if b<r:
      r = b
if r==1001:
  r = -1
print(r)