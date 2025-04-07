def round_half_up(n):
  if n-int(n)>=0.5:
    return int(n)+1
  else:
    return int(n)

while True:
  K, J, T, D = map(int, input().split())
  if K+J+T+D==0: break

  min_k, max_k = 0, 0
  if J>0:
    min_k += (J-0.5)*9
    max_k += (J+0.49)*9
  if T>0:
    min_k += (T-0.5)*4
    max_k += (T+0.49)*4
  if D>0:
    min_k += (D-0.5)*4
    max_k += (D+0.49)*4

  if round_half_up(min_k) <= K <= round_half_up(max_k):
    print('yes')
  else:
    print('no')