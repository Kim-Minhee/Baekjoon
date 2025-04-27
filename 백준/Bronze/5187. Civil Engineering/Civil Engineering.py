K = int(input())
for k in range(1, K+1):
  M, N = map(int, input().split())
  density = [int(input()) for _ in range(M)]

  total_density = 0
  for _ in range(N):
    H, W, D, I = map(int, input().split())
    total_density += H*W*D*density[I-1]

  print(f'Data Set {k}:')
  print(total_density)