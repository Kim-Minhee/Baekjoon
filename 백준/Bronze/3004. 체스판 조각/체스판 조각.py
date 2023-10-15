n = int(input())
a = n//2+1
if n%2==0:
  r = a**2
else:
  r = a*(a+1)
print(r)