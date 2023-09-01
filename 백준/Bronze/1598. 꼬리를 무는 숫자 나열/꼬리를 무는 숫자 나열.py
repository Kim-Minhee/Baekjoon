n, m = map(int, input().split())
if n%4==0:
  n_r = 4
  n_c = n//4
else:
  n_r = n%4
  n_c = n//4+1
if m%4==0:
  m_r = 4
  m_c = m//4
else:
  m_r = m%4
  m_c = m//4+1
print(abs(n_r-m_r)+abs(n_c-m_c))