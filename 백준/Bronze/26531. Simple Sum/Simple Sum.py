q, a = map(str, input().split('='))
if eval(q)==int(a):
  print('YES')
else:
  print('NO')