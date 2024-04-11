N, S = int(input()), input()
while 1:
  if S.count('s')==S.count('t'):
    print(S)
    break
  else:
    S = S[1:]