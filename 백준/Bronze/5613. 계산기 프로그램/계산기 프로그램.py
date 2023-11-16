def cal(num1, num2, oper):
  if oper=='+':
    r = num1+num2
  elif oper=='-':
    r = num1-num2
  elif oper=='*':
    r = num1*num2
  elif oper=='/':
    r = num1//num2
  return r

i, num, oper = 0, list(), list()
while 1:
  if i%2==0:
    num.append(int(input()))
  else:
    o = input()
    if o!='=':
      oper.append(o)
    else:
      break
  i += 1

r = num[0]
for i in range(len(oper)):
  r = cal(r, num[i+1], oper[i])
print(r)