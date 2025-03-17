while True:
  NMK = input()
  if NMK=='0 0 0': break
  n, m, k = map(int, NMK.split())
  P = list(map(int, input().split()))
  r = n
  for i in range(m-1):
    n += P[i%k]
    r += n
  print(r)