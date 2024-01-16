num, cnt = input(), 0
while 1:
  n = int(num[0])
  for i in range(1, len(num)):
    n *= int(num[i])
  if int(num)!=n:
    num = str(n)
  else:
    break
  cnt += 1
print(cnt)