N, M = map(int, input().split())
cubes = []
for _ in range(M):
  cubes.append(list(map(int, input().split())))

cnt = 0
for cube in cubes:
  i, j, k = map(int, cube)
  temp_cubes = [[i+1, j, k], [i-1, j, k], [i, j+1, k], [i, j-1, k], [i, j, k+1], [i, j, k-1]]
  chk = True
  for temp in temp_cubes:
    if temp not in cubes:
      chk = False
      break
  if chk:
    cnt += 1

print(cnt)