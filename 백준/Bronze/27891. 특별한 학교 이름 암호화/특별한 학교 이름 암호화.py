def cal_n(str1, str2):
  n = ord(str1)-ord(str2)
  if n<0: n += 26
  return n

S = input()

schools_init = ['NLCS', 'BHA', 'KIS', 'SJA']
schools_enc = ['northlondo', 'branksomeh', 'koreainter', 'stjohnsbur']

for i in range(4):
  n = cal_n(S[0], schools_enc[i][0])
  chk = True
  for j in range(1, 10):
    if cal_n(S[j], schools_enc[i][j])!=n:
      chk = False
      break
  if chk:
    print(schools_init[i])
    break