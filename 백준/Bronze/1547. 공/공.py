m = int(input())
cup = {1:1, 2:0, 3:0}
for _ in range(m):
  c1, c2 = map(int, input().split())
  cup[c1], cup[c2] = cup[c2], cup[c1]
for k, v in cup.items():
  if v==1:
    print(k)
    break