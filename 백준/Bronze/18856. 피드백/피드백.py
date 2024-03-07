def chk(num):
  r = True
  for i in range(2, num):
    if num%i==0:
      r = False
      break
  return r

N = int(input())
a = [n for n in range(1, N+1)]
i = a[-1]
while 1:
  if chk(i):
    a[-1] = i
    break
  else:
    i += 1
print(N)
print(*a)