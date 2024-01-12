for _ in range(int(input())):
  d, n, s, p = map(int, input().split())
  if s*n>d+p*n:
    print('parallelize')
  elif s*n<d+p*n:
    print('do not parallelize')
  else:
    print('does not matter')