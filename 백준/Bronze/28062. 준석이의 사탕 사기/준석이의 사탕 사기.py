N, A = int(input()), list(map(int, input().split()))
if N==1 and A[0]%2==1:
  print(0)
else:
  r = sum(A)
  if r%2!=0:
    odds = [a for a in A if a%2==1]
    odds.sort()
    r -= odds[0]
  print(r)