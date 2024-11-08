for i in range(1, int(input())+1):
  L = list(input().split())
  L = L[::-1]
  print(f'Case #{i}:', *L)