t = int(input())
for _ in range(t):
  num = list(map(int, input().split()))
  even = list()
  for n in num:
    if n%2==0:
      even.append(n)
  even.sort()
  print(sum(even), even[0])