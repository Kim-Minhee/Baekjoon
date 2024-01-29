def plus(num):
  r = 0
  for n in range(1, num+1):
    r += n
  return r

a, b = map(int, input().split())
r = plus(a)
for i in range(a+1, b+1):
  r *= plus(i)
print(r%14579)