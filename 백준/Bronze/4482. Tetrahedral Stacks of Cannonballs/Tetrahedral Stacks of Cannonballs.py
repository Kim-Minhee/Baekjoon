for i in range(int(input())):
  K = int(input())
  r = 0
  for k in range(1, K+1):
    r += k*(k+1)//2

  print(f'{i+1}: {K} {r}')