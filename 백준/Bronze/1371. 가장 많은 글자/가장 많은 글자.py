import sys
import string

a = dict()
for i in string.ascii_lowercase:
  a[i] = 0

s = sys.stdin.read()
s = s.replace('\n', '').replace(' ', '')
for i in s:
  if i in list(a.keys()):
    a[i] += 1
m = max(list(a.values()))

r = ''
for i in list(a.keys()):
  if a[i]==m:
    r += i
print(r)