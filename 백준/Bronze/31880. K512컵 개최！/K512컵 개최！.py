N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

r = sum(A)
for b in B:
  if b==0:
    pass
  else:
    r *= b

print(r)