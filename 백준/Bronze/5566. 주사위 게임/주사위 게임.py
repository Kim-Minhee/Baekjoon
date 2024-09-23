N, M = map(int, input().split())
N_LIST = [int(input()) for _ in range(N)]
M_LIST = [int(input()) for _ in range(M)]

d = 1
for i, m in enumerate(M_LIST):
  d += m
  if d>=N:
    print(i+1)
    break
  d += N_LIST[d-1]
  if d>=N:
    print(i+1)
    break