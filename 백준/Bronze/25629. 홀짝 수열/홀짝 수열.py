N = int(input())
L = list(map(int, input().split()))
odd, even = list(), list()
for l in L:
  if l%2==0:
    even.append(l)
  else:
    odd.append(l)
if len(odd)==len(even) or len(odd)-len(even)==1:
  print(1)
else:
  print(0)