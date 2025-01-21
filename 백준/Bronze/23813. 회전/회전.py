N = input()

r = 0
for _ in range(len(N)):
  N = N[-1]+N[:-1]
  r += int(N)

print(r)