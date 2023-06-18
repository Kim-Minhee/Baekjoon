s = int(input())
a = int(input())
b = int(input())
h, c = a, 0
while h<s:
  h += b
  c += 1
p = 100*c + 250
print(p)