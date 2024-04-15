N, X = map(int, input().split())
T = list(map(int, input().split()))
n = 1
while 1:
  if X>T[n-1]:
    print(n)
    break
  X += 1
  n += 1
  if n>N:
    n -= N