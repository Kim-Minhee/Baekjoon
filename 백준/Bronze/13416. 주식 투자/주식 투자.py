for _ in range(int(input())):
  bnf = 0
  for _ in range(int(input())):
    a, b, c = map(int, input().split())
    m = max(a, b, c)
    if m>0:
      bnf += m
  print(bnf)