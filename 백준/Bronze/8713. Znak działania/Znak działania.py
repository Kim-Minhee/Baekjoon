def chk_minus(num):
  if num<0:
    return '('+str(num)+')'
  return str(num)

A, B = map(int, input().split())

add, sub, mul = A+B, A-B, A*B
cals = set([add, sub, mul])

if len(cals)<3:
  print('NIE')
else:
  A = chk_minus(A)
  B = chk_minus(B)
  
  if add==max(cals):
    add = chk_minus(add)
    print(f'{A}+{B}={add}')
  elif sub==max(cals):
    sub = chk_minus(sub)
    print(f'{A}-{B}={sub}')
  else:
    mul = chk_minus(mul)
    print(f'{A}*{B}={mul}')