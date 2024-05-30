K = int(input())
for _ in range(K):
  r = 'G'*K
  r += '.'*3*K
  print(r)
for _ in range(K):
  r = '.'*K
  r += 'I'*K
  r += '.'*K
  r += 'T'*K
  print(r)
for _ in range(K):
  r = '.'*2*K
  r += 'S'*K
  r += '.'*K
  print(r)