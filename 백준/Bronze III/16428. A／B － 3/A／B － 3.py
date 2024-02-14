a, b = map(int, input().split())
if a<0 and b>0:
  q = -(abs(a)//b+1)
elif a>0 and b<0:
  q = -(a//abs(b))
elif a<0 and b<0:
  q = abs(a)//abs(b)+1
else:
  q = a//b
r = a-q*b
print(q)
print(r)