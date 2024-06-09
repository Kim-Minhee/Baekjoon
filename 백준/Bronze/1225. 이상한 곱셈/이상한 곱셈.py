A, B = map(str, input().split())
if len(A)<len(B):
  A, B = B, A
a, b = 0, 0
for i in A:
  a += int(i)
for j in B:
  b += a*int(j)
print(b)