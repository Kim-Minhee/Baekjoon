N = int(input())
X1, Y1 = map(int, input().split())

x2, y2, min_dist = int(), int(), float()
for i in range(N-1):
  X, Y = map(int, input().split())
  dist = ((X1-X)**2 + (Y1-Y)**2)**(1/2)
  if i==0 or min_dist>dist:
    x2, y2, min_dist = X, Y, dist

print(X1, Y1)
print(x2, y2)
print(f'{min_dist:.2f}')