while 1:
  try:
    N, P = map(int, input().split())

    p1, p2 = [], []
    for n in range(1, N//2+1, 2):
      p1.append([n, n+1])
    for n in range(N//2+1, N+1, 2):
      p2.append([n, n+1])
    p2.reverse()

    p = []
    for i in range(len(p1)):
      p.append(p1[i]+p2[i])

    for i in range(len(p1)):
      if P in p[i]:
        p[i].remove(P)
        print(*p[i])
        break
  except:
    break