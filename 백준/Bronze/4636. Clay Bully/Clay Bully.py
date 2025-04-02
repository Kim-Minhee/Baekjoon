while True:
  N = int(input())
  if N==-1:
    break

  clay = []
  name = []
  for i in range(N):
    I = input().split()
    clay.append(int(I[0])*int(I[1])*int(I[2]))
    name.append(I[3])

  max_index = clay.index(max(clay))
  min_index = clay.index(min(clay))
  print(f'{name[max_index]} took clay from {name[min_index]}.')