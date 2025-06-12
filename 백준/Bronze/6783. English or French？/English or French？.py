t_cnt, s_cnt = 0, 0

for _ in range(int(input())):
  S = input().lower()
  t_cnt += S.count('t')
  s_cnt += S.count('s')
  
if t_cnt>s_cnt:
  print('English')
else:
  print('French')