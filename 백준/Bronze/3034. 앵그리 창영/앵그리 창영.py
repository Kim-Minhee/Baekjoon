n, w, h = map(int, input().split())
l = (w**2+h**2)**(1/2)
for _ in range(n):
  s = int(input())
  if s<=l:
    print('DA')
  else:
    print('NE')