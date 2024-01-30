ms, mc, ml, num = -1, 51, 180, 0
for i in range(1, int(input())+1):
  s, c, l = map(int, input().split())
  if s>ms or (s==ms and c<mc) or (s==ms and c==mc and l<ml):
    ms, mc, ml, num = s, c, l, i
print(num)