T = int(input())
for i in range(1, T+1):
  N, M = map(int, input().split())

  cnt = M-N+1
  r = (M+N)*(cnt//2)
  if cnt%2!=0:
    r += N+cnt//2

  if i>1:
    print()
  print(f'Scenario #{i}:')
  print(r)