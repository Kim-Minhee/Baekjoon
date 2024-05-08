A, B, C = map(int, input().split())
if C==0:
  print(int((A+B)**(1/2)))
else:
  print(C**2-max(A, B))