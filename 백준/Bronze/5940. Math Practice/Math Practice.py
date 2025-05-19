A, B = map(int, input().split())

e = 0
for i in range(A+1, 63):
  if str(2**i)[0]==str(B):
    e = i
    break
print(e)