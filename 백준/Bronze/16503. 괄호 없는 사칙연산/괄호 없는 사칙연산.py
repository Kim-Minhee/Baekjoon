def oper(n1, o, n2):
  if o=='+':
    return n1+n2
  elif o=='-':
    return n1-n2
  elif o=='*':
    return n1*n2
  elif o=='/':
    return -1*(abs(n1)//abs(n2)) if n1*n2<0 else n1//n2

l = list(input().split())
r1_t = oper(int(l[0]), l[1], int(l[2]))
r1 = oper(r1_t, l[3], int(l[4]))
r2_t = oper(int(l[2]), l[3], int(l[4]))
r2 = oper(int(l[0]), l[1], r2_t)
print(min(r1, r2))
print(max(r1, r2))