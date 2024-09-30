import string
a = string.ascii_lowercase

while 1:
  S = input().lower()
  if S=='#': break
  r = list()
  for s in S:
    if s in a and s not in r:
      r.append(s)
  print(len(r))