def cal_y(num):
  l = [1, num]
  for i in range(2, int(num**(1/2))+1):
    if num%i==0:
      if i not in l:
        l.append(i)
      if num//i not in l:
        l.append(num//i)
  return len(l)

while True:
  M, N = map(int, input().split())
  if M==N==0: break

  max_x, max_y = 0, 0
  for x in range(N, M-1, -1):
    y = cal_y(x)
    if max_y<y:
      max_y = y
      max_x = x
    elif max_y==y and max_x<x:
      max_x = x
  
  print(max_x, max_y)