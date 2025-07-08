def closest_n(n, height):
  n1 = n//height*height
  n2 = n1+height
  n1_diff = abs(n-n1)
  n2_diff = abs(n-n2)
  if n1==0 or n2_diff<n1_diff:
    return n2_diff, n2
  elif n%height==0:
    return 0, n1
  else:
    return n1_diff, n1

N = int(input())
H = list(map(int, input().split()))

min_diff, block_h, close_n = N, int(), int()
for i, h in enumerate(H):
  diff, n = closest_n(N, h)
  if i==0 or diff<min_diff:
    min_diff = diff
    block_h = h
    close_n = n

print(block_h, close_n)