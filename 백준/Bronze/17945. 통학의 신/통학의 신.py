A, B = map(int, input().split())
x1 = int((-2*A+(4*A*A-4*B)**(1/2))//2)
x2 = int((-2*A-(4*A*A-4*B)**(1/2))//2)
if x1!=x2:
  print(min(x1, x2), max(x1, x2))
else:
  print(x1)