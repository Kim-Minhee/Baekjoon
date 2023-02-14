n = int(input())
k = int(input())
if k+60>=n:
  r = n*1500
else:
  r = (k+60)*1500
  r += (n-k-60)*3000
print(r)