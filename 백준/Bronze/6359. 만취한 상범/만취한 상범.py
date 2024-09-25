for _ in range(int(input())):
  N = int(input())
  room = [0]+[1]*N
  for k in range(2, N+1):
    for j in range(k, N+1, k):
      if room[j]:
        room[j] = 0
      else:
        room[j] = 1
  print(sum(room))