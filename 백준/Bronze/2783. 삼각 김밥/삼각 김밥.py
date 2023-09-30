x, y = map(int, input().split())
p = x/y
n = int(input())
for _ in range(n):
  x_i, y_i = map(int, input().split())
  if (x_i/y_i)<p:
    p = x_i/y_i
print(f'{round(1000*p, 2):.2f}')