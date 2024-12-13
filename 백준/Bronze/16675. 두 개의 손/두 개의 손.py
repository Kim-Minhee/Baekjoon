def winner(a, b):
  if srp[a]-srp[b]==1 or srp[a]-srp[b]==-2: # a win
    return 1
  elif srp[a]-srp[b]==-1 or srp[a]-srp[b]==2: # b win
    return -1
  else: # draw
    return 0

ML, MR, TL, TR = input().split()

srp = {'S':1, 'R':2, 'P':3}

if ML==MR and (winner(TL, ML)==1 or winner(TR, ML)==1):
  print('TK')
elif TL==TR and (winner(ML, TL)==1 or winner(MR, TL)==1):
  print('MS')
else:
  print('?')