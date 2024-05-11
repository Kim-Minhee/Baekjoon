import string

d = dict()
for a in string.ascii_lowercase:
  d[a] = 0

N = int(input())
S = input()
for s in S:
  if s in d:
    d[s] += 1
print(max(d.values()))