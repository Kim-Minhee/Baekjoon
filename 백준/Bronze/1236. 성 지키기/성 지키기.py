n, m = map(int, input().split())
w, h = list(range(m)), list(range(n))

for i in range(n):
  s = input()
  for j in range(len(s)):
    if s[j]=='X':
      if j in w:
        w.remove(j)
      if i in h:
        h.remove(i)

print(max(len(w), len(h)))