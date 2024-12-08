import re

N = int(input())

scores = []
for _ in range(N):
  Q = input()
  Q = int(re.sub(r'[06]', '9', Q))
  if Q>100: Q = 100
  scores.append(Q)

avg = sum(scores)/N
if avg-(avg//1)>=0.5:
  avg = avg//1+1
else:
  avg = avg//1

print(int(avg))