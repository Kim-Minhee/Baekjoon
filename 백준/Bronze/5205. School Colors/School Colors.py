K = int(input())
for k in range(1, K+1):
  N = int(input())
  RGB = []
  for _ in range(N):
    RGB.append(tuple(map(int, input().split())))
  
  distances = []
  max_dist = 0
  for i in range(N-1):
    for j in range(i+1, N):
      dist = (RGB[i][0]-RGB[j][0])**2+(RGB[i][1]-RGB[j][1])**2+(RGB[i][2]-RGB[j][2])**2
      distances.append((i, j, dist))
      if dist>max_dist: max_dist = dist

  print(f'Data Set {k}:')
  for i, j, d in distances:
    if d==max_dist:
      print(i+1, j+1)