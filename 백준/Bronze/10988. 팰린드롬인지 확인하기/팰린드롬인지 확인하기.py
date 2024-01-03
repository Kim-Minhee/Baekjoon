w, chk = input(), True
for i in range(len(w)//2):
  if w[i]!=w[-(i+1)]:
    chk = False
if chk:
  print(1)
else:
  print(0)