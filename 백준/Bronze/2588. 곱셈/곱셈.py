a, b = int(input()), int(input())
for b_ in str(b)[::-1]:
  print(a*int(b_))
print(a*b)