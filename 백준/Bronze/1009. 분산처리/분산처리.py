d = {0:[10], 1:[1], 2:[2, 4, 8, 6], 3:[3, 9, 7, 1], 4:[4, 6], 5:[5], 6:[6], 7:[7, 9, 3, 1], 8:[8, 4, 2, 6], 9:[9, 1]}

for _ in range(int(input())):
  A, B = map(int, input().split())
  a = int(str(A)[-1])
  c = B%len(d[a])-1
  print(d[a][c])