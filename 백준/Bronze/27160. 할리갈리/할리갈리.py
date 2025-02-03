import sys

s = {'STRAWBERRY':0, 'BANANA':0, 'LIME':0, 'PLUM':0}

for _ in range(int(sys.stdin.readline())):
  S, X = sys.stdin.readline().split()
  s[S] += int(X)

if 5 in s.values():
  print('YES')
else:
  print('NO')