for k in range(int(input())):
  N, W = map(int, input().split())
  S = list(map(int, input().split()))

  moving_average = []
  for i in range(N-W+1):
    s = S[i:i+W]
    moving_average.append(sum(s)//len(s))

  if k!=0:
    print()
  print(f'Data Set {k+1}:')
  print(max(moving_average)-min(moving_average))