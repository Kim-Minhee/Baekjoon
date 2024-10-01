def chk_prime(num):
  chk = True
  for i in range(2, int(num**(1/2))+1):
    if num%i==0:
      chk = False
      break
  return chk

P, N = map(str, input().split())
old, new = int(P), int(N+P)
if chk_prime(old) and chk_prime(new):
  print('Yes')
else:
  print('No')