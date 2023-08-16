n = int(input())
ls = list(map(int, input().split()))
r = list()
for l in ls:
  if l>=300:
    r.append(1)
  elif l>=275:
    r.append(2)
  elif l>=250:
    r.append(3)
  else:
    r.append(4)
print(*r)