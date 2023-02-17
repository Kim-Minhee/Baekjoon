n, w, h, l = map(int, input().split())
w = w//l
h = h//l
if w*h>=n:
  print(n)
else:
  print(w*h)