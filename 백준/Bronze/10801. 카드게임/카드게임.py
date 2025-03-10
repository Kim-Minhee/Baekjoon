A = list(map(int, input().split()))
B = list(map(int, input().split()))

score_a, score_b = 0, 0
for i in range(10):
  a, b = A[i], B[i]
  if a>b: score_a += 1
  elif a<b: score_b += 1

if score_a>score_b: print('A')
elif score_a<score_b: print('B')
else: print('D')