N = int(input())

pulleys = []
for _ in range(N-1):
  pulleys.append(tuple(map(int, input().split())))

pulleys.sort()
r = 0
for pulley in pulleys:
  if pulley[-1]:
    r = 0 if r else 1

print(r)