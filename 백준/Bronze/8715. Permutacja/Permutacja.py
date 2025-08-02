N = int(input())
A = list(map(int, input().split()))

A.sort()
if A[0]==1 and A[-1]==N and len(set(A))==N:
  print('TAK')
else:
  print('NIE')