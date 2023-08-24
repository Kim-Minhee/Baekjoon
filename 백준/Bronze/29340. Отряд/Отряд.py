a, b = input(), input()
r = ''
for i in range(len(a)):
  r += str(max(int(a[i]), int(b[i])))
print(r)