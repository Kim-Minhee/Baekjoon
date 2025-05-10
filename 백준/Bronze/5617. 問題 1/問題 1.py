tris = [0, 0, 0, 0]
is_existing = True
try:
  while True:
    lines = list(map(int, input().split()))
    if is_existing:
      lines.sort()
      a, b, c = lines[0], lines[1], lines[2]
      if a+b<=c:
        is_existing = False
      else:
        tris[0] += 1
        d = a**2 + b**2
        if d==c**2: tris[1] += 1
        elif d>c**2: tris[2] +=1
        else: tris[3] += 1

      if not is_existing:
        print(*tris)
except:
  exit()