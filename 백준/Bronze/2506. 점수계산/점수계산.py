n = int(input())
ox = list(map(int, input().split()))
s, c = list(), 0
for i in ox:
  if i==1:
    s.append(1+c)
    c += 1
  else:
    c = 0
print(sum(s))