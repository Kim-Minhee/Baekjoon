alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while True:
  S = input()
  if S=='END': break

  check = True
  for i in range(26):
    if S.count(alphabet[i])>1:
      check = False
      break
  
  if check:
    print(S)