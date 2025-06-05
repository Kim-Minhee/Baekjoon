while True:
  N = int(input())
  if N==0: break
  
  s_N = sum(int(i) for i in str(N))
  p = 11
  while True:
    n = N*p
    s_n = sum(int(i) for i in str(n))
    if s_N==s_n:
      print(p)
      break
    p += 1