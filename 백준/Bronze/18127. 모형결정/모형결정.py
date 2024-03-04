A, B = map(int, input().split())
r = 1
for i in range(1, B+1):
  r += i+1
  r += (A-3)*i
print(r)