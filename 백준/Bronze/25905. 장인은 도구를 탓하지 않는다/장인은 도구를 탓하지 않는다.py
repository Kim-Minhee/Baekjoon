P = []
for _ in range(10):
  P.append(float(input()))
P.sort(reverse=True)

r = 10**9
for i in range(9):
  r *= P[i]/(i+1)
print(r)