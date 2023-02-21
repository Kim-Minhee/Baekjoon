x1, y1, z1 = map(int, input().split())
x2, y2, z2 = map(int, input().split())

if x2>=x1 and y2>=y1 and z2>=z1:
  print('A')
elif x2>=(x1/2) and y2>=y1 and z2>=z1:
  print('B')
elif y2>=y1 and z2>=z1:
  print('C')
elif y2>=(y1/2) and z2>=z1:
  print('D')
elif z2>=z1:
  print('E')