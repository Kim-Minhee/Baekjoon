d = {'black':0, 'brown':1, 'red':2, 'orange':3, 'yellow':4, 'green':5, 'blue':6, 'violet':7, 'grey':8, 'white':9}
r = ''
for i in range(3):
  c = input()
  if i<2:
    r += str(d[c])
  else:
    r += '0'*d[c]
print(int(r))