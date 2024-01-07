n = int(input())
s = '* '*n
for i in range(1, n+1):
  if i%2!=0:
    print(s[:-1])
  else:
    print(' '+s[:-1])