S = input()

while True:
  try:
      L = input()
      temp_s = ''
      for i, l in enumerate(L):
        s = int(S[i])+int(l)
        if s>9: s-=10
        temp_s += str(s)
      S = temp_s
  except:
    break

print(S)