for _ in range(int(input())):
  X, Y = input().split()
  r = int(X[::-1]) + int(Y[::-1])
  r = int(str(r)[::-1])
  print(r)