n, m = map(int, input().split())
alst = list(map(int, input().split()))
r = 1
for a in alst:
  r *= a%m
print(r%m)