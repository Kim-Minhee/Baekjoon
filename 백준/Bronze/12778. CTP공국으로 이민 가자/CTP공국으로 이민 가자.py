for _ in range(int(input())):
  N, M = map(str, input().split())
  r = []

  if M=='C':
    L = list(map(str, input().split()))
    for l in L:
      r.append(ord(l)-64)
  else:
    L = list(map(int, input().split()))
    for l in L:
      r.append(chr(l+64))
  
  print(*r)