t = int(input())
for i in range(1, t+1):
  l = list(map(int, input().split()))
  l.sort()
  if l[0]+l[1]<=l[2]:
    print(f'Case #{i}: invalid!')
  elif l[0]==l[1]==l[2]:
    print(f'Case #{i}: equilateral')
  elif l[0]==l[1] or l[1]==l[2]:
    print(f'Case #{i}: isosceles')
  else:
    print(f'Case #{i}: scalene')