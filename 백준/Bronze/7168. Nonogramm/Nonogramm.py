def count_black(nono):
  blacks = list(nono.split('.'))
  r = []
  for black in blacks:
    if black!='':
      r.append(str(len(black)))
  if r==[]:
    r = ['0']
  return r

N, M = map(int, input().split())

nonogramm = []
n_results = []
for _ in range(N):
  NONO = input()
  n_results.append(count_black(NONO))
  nonogramm.append(NONO)

for n in n_results:
  print(' '.join(n))

m_nonogramm = []
for i in range(M):
  nono = ''
  for j in range(N):
    nono += nonogramm[j][i]
  m_nonogramm.append(nono)

for nono in m_nonogramm:
  r = count_black(nono)
  print(' '.join(r))