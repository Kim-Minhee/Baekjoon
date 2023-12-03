while 1:
  m, a, b = map(int, input().split())
  if m==a==b==0:
    break
  t = m/a-m/b
  h = int(t)
  m_ = (t-h)*60
  m = int(m_)
  s = round((m_-m)*60)
  if m<10:
    m = '0'+str(m)
  if s<10:
    s = '0'+str(s)
  print(f'{h}:{m}:{s}')