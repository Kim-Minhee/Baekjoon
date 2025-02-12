N = int(input())
P = list(map(int, input().split()))

stric_chk = [True]*N
max_stric, stric = 0, 0
for i, p in enumerate(P):
  if p==0:
    if stric_chk[i]:
      if i+1<N: stric_chk[i+1] = False
    else:
      stric = 0
  else:
    stric += 1

  if max_stric<stric:
    max_stric = stric

print(max_stric)