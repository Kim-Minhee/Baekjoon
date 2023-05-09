import string
func = list(string.ascii_uppercase)
para = list(string.ascii_lowercase)

oldP = list(input())
newP = list()
for a in oldP:
  if a in func:
    if len(newP)%4!=0:
      while len(newP)%4!=0:
        newP.append('NOP')
    newP.append(a)
  elif a in para:
    newP.append(a)
print(newP.count('NOP'))