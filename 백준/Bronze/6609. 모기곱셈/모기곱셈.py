try:
  while 1:
    M, P, L, E, R, S, N = map(int, input().split())
    for _ in range(N):
      e = M*E
      M = P//S
      P = L//R
      L = e

    print(M)
except:
  exit()