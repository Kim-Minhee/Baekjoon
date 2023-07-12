n = int(input())
c = list(map(int, input().split()))
r = 0
for a in c:
  if a>n:
    r += n
  else:
    r += a
print(r)