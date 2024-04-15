N = int(input())
A = list(map(int, input().split()))
v = 0
for a in A:
  v = 1-(1-v)*(1-a/100)
  print(v*100)