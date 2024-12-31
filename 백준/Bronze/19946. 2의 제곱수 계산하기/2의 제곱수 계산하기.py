N = int(input())
l = []
for i in range(0, 65):
  l.append((2**i-1)*2**(64-i))
print(l.index(N))