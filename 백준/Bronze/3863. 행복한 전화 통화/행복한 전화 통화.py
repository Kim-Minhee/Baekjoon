while True:
  n, m = map(int, input().split())
  if n==0 and m==0:
    break
  
  info = list()
  for _ in range(n):
    f, t, s, d = map(int, input().split())
    info.append([s, s+d])
  
  pol = list()
  for _ in range(m):
    s, d = map(int, input().split())
    pol.append([s, s+d])
  
  cnt = list()
  for s_p, e_p in pol:
    c = 0
    for s_i, e_i in info:
      if s_p<e_i and e_p>s_i:
        c += 1
    cnt.append(c)
  
  for c in cnt:
    print(c)