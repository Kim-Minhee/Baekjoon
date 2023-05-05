def findRC(n):
  y = list()
  for i in range(1, n+1):
    if n%i==0:
      y.append(i)
  if len(y)%2==0:
    r = y[len(y)//2-1]
    c = y[len(y)//2]
  else:
    r = y[len(y)//2]
    c = y[len(y)//2]
  return r, c

m = input()
r, c = findRC(len(m))
m_list = list()
for i in range(0, len(m), r):
  m_list.append(m[i:i+r])

s = str()
for i in range(r):
  for j in range(c):
    s += m_list[j][i]
print(s)