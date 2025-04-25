K = int(input())
for k in range(1, K+1):
  N, M = map(int, input().split())

  machine_m = [tuple(map(int, input().split())) for _ in range(M)]

  machine_n = [0]*M
  for _ in range(N):
    machine_n[int(input())-1] += 1

  machine_r = []
  for i in range(M):
    p, c, u, r = machine_m[i]
    num = machine_n[i]
    if num>u: num = u
    if (r*num)>(p+c*num):
      machine_r.append(i+1)

  if k!=1: print()
  print(f'Data Set {k}:')
  for r in machine_r:
    print(r)