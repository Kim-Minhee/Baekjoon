h = 0
for _ in range(int(input())):
  s, a = map(int, input().split())
  h += a%s
print(h)