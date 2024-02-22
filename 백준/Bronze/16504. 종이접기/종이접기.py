r = 0
for _ in range(int(input())):
  l = list(map(int, input().split()))
  r += sum(l)
print(r)