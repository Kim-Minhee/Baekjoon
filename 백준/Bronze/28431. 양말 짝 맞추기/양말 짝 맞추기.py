s = list()
for _ in range(5):
  n = int(input())
  if n in s:
    s.remove(n)
  else:
    s.append(n)
print(s[0])