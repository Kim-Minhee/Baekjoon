N, S = input().split()

r = 0
for _ in range(int(N)):
  I, C = input().split()
  if S in I.split('_'):
    r += int(C)

print(r)