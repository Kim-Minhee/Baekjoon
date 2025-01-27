N = int(input())

if N<=28:
  for i in range(1, N+1):
    if sum(range(1, i+1))>=N:
      print(i)
      break
else:
  print((N-29)//7+8)