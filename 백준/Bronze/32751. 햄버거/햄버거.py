N = input()
A, B, C, D = map(int, input().split())
S = input()

chk = False
if S.count('a')<=A and S.count('b')<=B and S.count('c')<=C and S.count('d')<=D:
  if 'aa' not in S and 'bb' not in S and 'cc' not in S and 'dd' not in S:
    if S[0]==S[-1]=='a':
      chk = True

if chk:
  print('Yes')
else:
  print('No')