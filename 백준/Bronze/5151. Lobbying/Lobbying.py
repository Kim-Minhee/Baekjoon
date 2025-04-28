K = int(input())
for k in range(1, K+1):
    N, M, T1 = map(int, input().split())

    d = [0]*N
    for _ in range(M):
      I, T2, D = map(float, input().split())
      if 0<=T1-T2<1000:
        d[int(I)-1] += D

    v = []
    for _ in range(N):
      v.append(input())

    y, n = 0, 0
    for i, vote in enumerate(v):
      if vote=='N':
        n += 1/(1+(d[i]/10000))
      else:
        y += 1

    if k!=1: print()
    print(f'Data Set {k}:')
    print(format(round(y, 2), '.2f'), format(round(n, 2), '.2f'))