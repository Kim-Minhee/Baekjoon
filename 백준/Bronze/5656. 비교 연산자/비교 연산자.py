def cal(a, b, o):
  if o=='>':
    return a>b
  elif o=='>=':
    return a>=b
  elif o=='<':
    return a<b
  elif o=='<=':
    return a<=b
  elif o=='==':
    return a==b
  elif o=='!=':
    return a!=b

i = 0
while 1:
  C = list(map(str, input().split()))

  if C[1]=='E':
    break
  i += 1
  r = cal(int(C[0]), int(C[2]), C[1])
  if r:
    print(f'Case {i}: true')
  else:
    print(f'Case {i}: false')