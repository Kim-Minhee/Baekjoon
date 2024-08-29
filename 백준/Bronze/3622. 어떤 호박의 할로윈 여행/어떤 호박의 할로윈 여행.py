# 입력
AO, AI, BO, BI, P = map(int, input().split())

# 풀이
if AO<BO:
  AO, BO = BO, AO
  AI, BI = BI, AI

chk = False
if AO<=P and BO<=AI:
  chk = True
elif AO+BO<=P:
  chk = True

# 출력
if chk:
  print('Yes')
else:
  print('No')