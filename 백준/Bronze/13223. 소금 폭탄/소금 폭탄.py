def strTime(a):
  if a<10:
    return '0'+str(a)
  else:
    return str(a)

h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))
t1, t2 = h1*3600+m1*60+s1, h2*3600+m2*60+s2
if t1>t2:
  t2 += 86400
t = t2-t1
h, m, s = t//3600, (t%3600)//60, t%60
if h==m==s==0:
  print('24:00:00')
else:
  print(strTime(h)+':'+strTime(m)+':'+strTime(s))