X, Y = (map(int, input().split()))
K = int(input())
M = input()

luka = [(X-1, Y+1), (X, Y+1), (X+1, Y+1),
        (X-1, Y), (X, Y), (X+1, Y),
        (X-1, Y-1), (X, Y-1), (X+1, Y-1)]

ttm, time = [0, 0], []

if tuple(ttm) in luka:
    time.append(0)

for i, move in enumerate(M):
  if move=='I': ttm[0] += 1
  elif move=='S': ttm[1] += 1
  elif move=='Z': ttm[0] -= 1
  elif move=='J': ttm[1] -= 1

  if tuple(ttm) in luka:
    time.append(i+1)

if len(time)==0:
  print(-1)
else:
  for t in time:
    print(t)