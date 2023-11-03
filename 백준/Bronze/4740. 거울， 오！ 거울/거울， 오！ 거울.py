while 1:
  s = input()
  if s=='***':
    break
  s = list(s)
  r = str()
  for i in reversed(s):
    r += i
  print(r)