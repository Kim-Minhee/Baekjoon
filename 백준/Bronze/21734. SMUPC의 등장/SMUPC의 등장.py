S = input()
for s in S:
  num = str(ord(s))
  c = 0
  for n in num: c += int(n)
  print(s*c)