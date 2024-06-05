import string

a = dict()
for i in string.ascii_lowercase:
  a[i] = 0

for _ in range(int(input())):
  n = input()
  a[n[0]] += 1

r = ''
for i in string.ascii_lowercase:
  if a[i]>=5:
    r += i
if r=='':
  print('PREDAJA')
else:
  print(r)