gs, ss = [1, 2, 3, 3, 4, 10], [1, 2, 2, 2, 3, 5, 10]
t = int(input())
for i in range(t):
  g = list(map(int, input().split()))
  s = list(map(int, input().split()))
  gts = sts = 0
  for gi in range(6):
    gts += gs[gi]*g[gi]
  for si in range(7):
    sts += ss[si]*s[si]
  if gts>sts:
    print(f'Battle {i+1}: Good triumphs over Evil')
  elif sts>gts:
    print(f'Battle {i+1}: Evil eradicates all trace of Good')
  else:
    print(f'Battle {i+1}: No victor on this battle field')