import string

alp_d, i = dict(), 65
for a in list(string.ascii_uppercase):
  alp_d[a] = i
  i += 1

t = int(input())
for _ in range(t):
  word, r, du = input(), sum(list(range(65, 91))), list()
  for w in word:
    if w not in du:
      r -= alp_d[w]
      du.append(w)
  print(r)