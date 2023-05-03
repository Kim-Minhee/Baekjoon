r = int(input())
sg = list(input())
n = int(input())
fs = list()
for _ in range(n):
  f = list(input())
  fs.append(f)

sg_s = 0
for i in range(n):
  for j in range(r):
    sg_ = sg[j]
    fs_ = fs[i][j]
    if sg_ == fs_:
      sg_s += 1
    elif ((sg_=='S')and(fs_=='P'))or((sg_=='P')and(fs_=='R'))or((sg_=='R')and(fs_=='S')):
      sg_s += 2
print(sg_s)

sg_m_s = 0
for i in range(r):
  fs_ = list()
  for j in range(n):
    fs_.append(fs[j][i])
  s_cnt = fs_.count('S')
  p_cnt = fs_.count('P')
  r_cnt = fs_.count('R')
  sg_s = s_cnt + 2*p_cnt
  sg_p = p_cnt + 2*r_cnt
  sg_r = r_cnt + 2*s_cnt
  sg_m_s += max(sg_s, sg_p, sg_r)
print(sg_m_s)