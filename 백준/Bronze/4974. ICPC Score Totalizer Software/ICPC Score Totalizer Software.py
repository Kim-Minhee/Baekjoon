while True:
  N = int(input())
  if N==0: break

  scores = []
  for _ in range(N):
    scores.append(int(float(input())))
  scores.sort()

  print(sum(scores[1:-1])//(N-2))