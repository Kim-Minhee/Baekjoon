def time(num):
  if num<10:
    return '0'+str(num)
  else:
    return num

CH, CM, CS = map(int, input().split(':'))
SH, SM, SS = map(int, input().split(':'))
s = SS-CS
if s<0:
  s += 60
  SM -= 1
m = SM-CM
if m<0:
  m += 60
  SH -= 1
h = SH-CH
if h<0:
  h += 24

s = time(s)
m = time(m)
h = time(h)
print(h, m, s, sep=':')