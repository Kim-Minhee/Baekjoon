N = int(input())
L = list(map(int, input().split()))
a, r, i = L.count(1), L.count(-1), L.count(0)
if i>=N/2:
  print('INVALID')
elif a>r:
  print('APPROVED')
else:
  print('REJECTED')