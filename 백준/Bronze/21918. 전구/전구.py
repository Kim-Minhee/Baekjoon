n, m = map(int, input().split())
s = [0]+list(map(int, input().split()))

for _ in range(m):
  a, b, c = map(int, input().split())
  if a==1:
    s[b] = c
  elif a==2:
    for i in range(b, c+1):
      if s[i]==0: s[i]=1
      else: s[i]=0
  elif a==3:
    for i in range(b, c+1):
      if s[i]==1: s[i]=0
  else:
    for i in range(b, c+1):
      if s[i]==0: s[i]=1

print(*s[1:])