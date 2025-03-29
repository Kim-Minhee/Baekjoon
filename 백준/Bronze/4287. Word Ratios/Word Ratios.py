alphabet = 'abcdefghijklmnopqrstuvwxyz'

while True:
  S = input()
  if S=='#':
    break
  
  a, b, c = S.split()
  d = ''
  for i in range(len(a)):
    n1 = alphabet.index(b[i])-alphabet.index(a[i])
    if n1<0:
      n1 += 26
    
    n2 = alphabet.index(c[i])+n1
    if n2>25:
      n2 -= 26
    
    d += alphabet[n2]

  print(a, b, c, d)