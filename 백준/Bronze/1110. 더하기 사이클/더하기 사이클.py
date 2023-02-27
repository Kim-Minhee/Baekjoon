# mango2님... 보고 계신가요...?

def newN(num):
  if len(num)==1:
    num = '0'+num
  newN = num[-1]+str(int(num[0])+int(num[-1]))[-1]
  return newN

n, c = input(), 0
ori = n
while True:
  c += 1
  new = newN(ori)
  if int(new)==int(n):
    break
  ori = new

print(c)