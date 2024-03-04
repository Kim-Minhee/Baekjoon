a, b, c = map(int, input().split())
l = [a, b, c, a*b, b*c, c*a, a*b*c]
odd, even = list(), list()
for n in l:
  if n%2==0:
    even.append(n)
  else:
    odd.append(n)
if len(odd)==0:
  print(max(even))
else:
  print(max(odd))