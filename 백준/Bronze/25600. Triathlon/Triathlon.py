n = int(input())
max_score = 0
for _ in range(n):
  a, d, g = map(int, input().split())
  score = a*(d+g)
  if a==(d+g):
    score *= 2
  if score>max_score:
    max_score = score
print(max_score)