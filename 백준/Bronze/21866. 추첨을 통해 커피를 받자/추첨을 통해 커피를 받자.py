max_score = [100, 100, 200, 200, 300, 300, 400, 400, 500]
score = list(map(int, input().split()))
r = 'none'
if sum(score)>=100:
  r = 'draw'
for i, s in enumerate(score):
  if s>max_score[i]:
    r = 'hacker'
    break
print(r)