n = int(input())
for i in range(1, 2*n+1, 2):
  s = ' '*((2*n-i)//2)
  s += '*'*i
  print(s)