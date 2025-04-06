while True:
  N, W, L, H, A, M = map(int, input().split())
  if N+W+L+H+A+M==0:
    break
  
  total_area = N*(W*L + 2*(L*H + H*W))
  for _ in range(M):
    a, b = map(int, input().split())
    total_area -= N*(a*b)
  
  if total_area%A==0:
    print(total_area//A)
  else:
    print(total_area//A+1)