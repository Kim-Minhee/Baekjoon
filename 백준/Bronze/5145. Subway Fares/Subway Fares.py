K = int(input())
for k in range(K):
  N = int(input())
  S = [int(input()) for _ in range(N-1)]
  NAME = [input() for _ in range(N)]
  D, A = input(), input()

  d_index = NAME.index(D)
  a_index = NAME.index(A)
  s_index = max(d_index, a_index)-min(d_index, a_index)
  fares = S[s_index-1]

  if k!=0: print()
  print(f'Data Set {k+1}:')
  print(fares)