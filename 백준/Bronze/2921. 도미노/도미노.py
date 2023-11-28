n = int(input())
dot = list()
for x in range(n+1):
  for y in range(x, n+1):
    dot.append(x)
    dot.append(y)
print(sum(dot))