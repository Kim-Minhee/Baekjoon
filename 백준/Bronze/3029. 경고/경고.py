def time_sum(h, m, s):
  s += m*60
  s += h*3600
  return s

def time_unit(num):
  if num<10:
    num = '0'+str(num)
  else:
    num = str(num)
  return num

nh, nm, ns = map(int, input().split(':'))
th, tm, ts = map(int, input().split(':'))

n = time_sum(nh, nm, ns)
t = time_sum(th, tm, ts)
if t<n:
  t += 24*3600
r = t-n

rh, rs = r//3600, r%3600
rm, rs = rs//60, rs%60
if rh==0 and rm==0 and rs==0:
  print('24:00:00')
else:
  rh, rm, rs = time_unit(rh), time_unit(rm), time_unit(rs)
  print(rh+':'+rm+':'+rs)