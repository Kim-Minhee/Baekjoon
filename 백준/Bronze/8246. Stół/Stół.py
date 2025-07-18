A, B, K = map(int, input().split())

a, b = A//K, B//K
if a==0 or b==0:
  chairs = 0
elif a==1 or b==1:
  chairs = a*b
else:
  chairs = 2*(a+b-2)

print(chairs)