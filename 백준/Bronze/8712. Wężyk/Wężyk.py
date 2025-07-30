N = int(input())

is_even = False
for n in range(1, N**2+1, N):
  zigzag = [str(j) for j in range(n, n+N)]
  if is_even:
    zigzag.reverse()
    is_even = False
  else:
    is_even = True
  print(' '.join(zigzag))