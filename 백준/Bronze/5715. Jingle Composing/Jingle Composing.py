length = {'W':1, 'H':1/2, 'Q':1/4, 'E':1/8, 'S':1/16, 'T':1/32, 'X':1/64}

while True:
  S = input()
  if S=='*': break

  s_list = S.split('/')
  r = 0
  for s in s_list:
    if sum(length[i] for i in s)==1:
      r += 1

  print(r)