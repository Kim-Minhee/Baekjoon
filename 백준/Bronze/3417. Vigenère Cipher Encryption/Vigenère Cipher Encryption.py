a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while True:
  K = input()
  if K=='0': break

  c = ''
  P = input()
  for i, p in enumerate(P):
    k = K[i%len(K)]
    c += a[(a.index(p)+a.index(k)+1)%26]

  print(c)