N, Q = map(int, input().split())

song = []
for i in range(N):
  B = int(input())
  for _ in range(B):
    song.append(i+1)

for _ in range(Q):
  T = int(input())
  print(song[T])