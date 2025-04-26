K = int(input())
for k in range(1, K+1):
  C, B, N, R = map(int, input().split())
  B_LIST = list(map(int, input().split()))
  N_LIST = [tuple(map(int, input().split())) for _ in range(N)]

  total_tax = 0
  for (c, p) in N_LIST:
    if c in B_LIST:
      total_tax += int(p*(R/100))

  if k!=1: print()
  print(f'Data Set {k}:')
  print(total_tax)