n = int(input())
p =int(input())
s = 0
if n>=5:
  s = 500
if n>=10:
  s_ = p*0.1
  if s_>s:
    s = s_
if n>=15:
  s_ = 2000
  if s_>s:
    s = s_
if n>=20:
  s_ = p*0.25
  if s_>s:
    s = s_
if p-s<=0:
  print(0)
else:
  print(int(p-s))