for k in range(int(input())):
  N = int(input())
  X = list(map(int, input().split()))
  Y = list(map(int, input().split()))

  dist = 0
  for i in range(N-1):
    for j in range(i+1, N):
      if Y[j]>=X[i]:
        dist = max(dist, j-i)
      else:
        break

  if k>0:
    print()
  print(f'The maximum distance is {dist}')