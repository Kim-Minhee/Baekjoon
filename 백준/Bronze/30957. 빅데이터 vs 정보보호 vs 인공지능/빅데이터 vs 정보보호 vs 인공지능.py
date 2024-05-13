a = {'B':0, 'S':0, 'A':0}
N = int(input())
S = input()
for s in S:
  a[s] += 1

m = max(a.values())
r = ''
for i in a.keys():
  if a[i]==m:
    r += i
if r=='BSA':
  print('SCU')
else:
  print(r)