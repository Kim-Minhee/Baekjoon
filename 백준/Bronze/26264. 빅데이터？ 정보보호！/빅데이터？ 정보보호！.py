N, S = int(input()), input()
big = sec = 0
while len(S)!=0:
  if S[0]=='s':
    sec += 1
    S = S[8:]
  else:
    big += 1
    S = S[7:]
if big>sec:
  print('bigdata?')
elif big<sec:
  print('security!')
else:
  print('bigdata? security!')