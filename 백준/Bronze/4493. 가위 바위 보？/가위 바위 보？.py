t = int(input())
for _ in range(t):
  n = int(input())
  s1 = s2 =0
  for _ in range(n):
    p1, p2 = input().split()
    if (p1=='R' and p2=='S') or (p1=='P' and p2=='R') or (p1=='S' and p2=='P'):
      s1 += 1
    elif (p2=='R' and p1=='S') or (p2=='P' and p1=='R') or (p2=='S' and p1=='P'):
      s2 += 1
  if s1>s2:
    print('Player 1')
  elif s2>s1:
    print('Player 2')
  else:
    print('TIE')