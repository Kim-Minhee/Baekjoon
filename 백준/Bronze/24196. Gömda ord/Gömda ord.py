import string
a = list(string.ascii_uppercase)
m = input()
i, r = 0, ''
while True:
  r += m[i]
  i += a.index(m[i])+1
  if i>=(len(m)):
    break
print(r)