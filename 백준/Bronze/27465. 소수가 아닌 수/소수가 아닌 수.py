N = int(input())
chk = True
while chk:
  for n in range(2, N):
    if N%n==0:
      print(N)
      chk = False
      break
  N += 1