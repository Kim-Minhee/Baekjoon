i = 0
while 1:
  S = input()
  if S=='Was it a cat I saw?': break
  i += 1
  r = ''
  for s in S[::i+1]:
    r += s
  print(r)