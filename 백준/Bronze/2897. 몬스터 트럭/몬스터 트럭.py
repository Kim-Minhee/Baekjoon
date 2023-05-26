r, c = map(int, input().split())
parking = list()
for _ in range(r):
  parking.append(input())

bc = [0, 0, 0 ,0 ,0]
for i in range(r-1):
  for j in range(c-1):
    p = [parking[i][j], parking[i][j+1], parking[i+1][j], parking[i+1][j+1]]
    if '#' not in p:
      bc[p.count('X')] += 1

for c in bc:
  print(c)