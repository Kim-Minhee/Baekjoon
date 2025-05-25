N = int(input())
cows = []
for _ in range(N):
  cows.append(tuple(map(int, input().split())))

cow1, cow2 = -1, -1
max_dist = 0
for i in range(N-1):
  for j in range(i+1, N):
    dist = (cows[i][0]-cows[j][0])**2+(cows[i][1]-cows[j][1])**2
    if dist>max_dist:
      cow1, cow2 = i+1, j+1
      max_dist = dist

print(cow1, cow2)