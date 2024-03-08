d1, d2, d3 = map(int, input().split())
b = (d1-d2+d3)/2
c = (d3-d1+d2)/2
a = (d2-d3+d1)/2

if a<=0 or b<=0 or c<=0:
  print(-1)
else:
  print(1)
  print(round(a, 1), round(b, 1), round(c, 1))