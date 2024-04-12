N = int(input())
print('int a;')
print('int *ptr = &a;')
for i in range(1, N):
  if i==1:
    print('int '+'*'*(i+1)+r'ptr{0} = &ptr;'.format(i+1))
  else:
    print('int '+'*'*(i+1)+r'ptr{0} = &ptr{1};'.format(i+1, i))