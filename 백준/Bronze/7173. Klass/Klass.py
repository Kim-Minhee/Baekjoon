M, N = map(int, input().split())
interest = [list(input()) for _ in range(M)]
focus = []

for row in range(M):
  for col in range(N):
    interest_mn = int(interest[row][col])

    sum_focus, cnt = 0, 0
    if row>0:
      sum_focus += abs(interest_mn-int(interest[row-1][col]))
      cnt += 1
    if row<M-1:
      sum_focus += abs(interest_mn-int(interest[row+1][col]))
      cnt += 1
    if col>0:
      sum_focus += abs(interest_mn-int(interest[row][col-1]))
      cnt += 1
    if col<N-1:
      sum_focus += abs(interest_mn-int(interest[row][col+1]))
      cnt += 1
    
    focus.append(sum_focus/cnt)

print(f'{sum(focus):.4f}')