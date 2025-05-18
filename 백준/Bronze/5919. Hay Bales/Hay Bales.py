N = int(input())
P = [int(input()) for _ in range(N)]

std = sum(P)//N
r = 0
for p in P:
  if p>std:
    r += p-std

print(r)