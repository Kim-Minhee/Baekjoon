for _ in range(int(input())):
  w, c = int(), int()
  for i in range(int(input())):
    W, C = map(int, input().split())

    if i==0:
      w, c = W, C
    else:
      if C/W<c/w or (C/W==c/w and C<c):
        w, c = W, C

  print(c)