while True:
  N = int(input())
  if N==0: break

  n = 1
  while True:
    sum_n = n*(n+1)//2
    if sum_n>=N:
      break
    n += 1

  r = 0
  for i in range(1, n):
    r += i**2
  r += n*(N-((n-1)*n//2))

  print(N, r)