S = input()

s = list(S.split('+'))
if len(s)==2 and s[0]==s[1]:
  try:
    n = int(s[0])
    if n!=0:
      print('CUTE')
    else:
      print('No Money')
  except:
    print('No Money')
else:
  print('No Money')