while True:
  T = int(input())
  if T==0: break

  lotto_num = [0]*49
  for _ in range(T):
    N = list(map(int, input().split()))
    for n in N:
      if not lotto_num[n-1]:
        lotto_num[n-1] = 1
  if sum(lotto_num)==49:
    print('Yes')
  else:
    print('No')