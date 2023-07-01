n = int(input())
for _ in range(n):
  x = int(input())
  total = float()
  for _ in range(x):
    name, num, cost = map(str, input().split())
    total += int(num)*float(cost)
  print(f'${round(total, 2):.2f}')