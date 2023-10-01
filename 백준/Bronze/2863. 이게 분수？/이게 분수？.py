def Cal(num):
  cal = (num[0]/num[2])+(num[1]/num[3])
  return cal

def Rot(num):
  rot = [num[2]]+[num[0]]+[num[3]]+[num[1]]
  return rot

num = list(map(int, input().split()))
num += list(map(int, input().split()))
cal, r = 0, 0
for i in range(4):
  cal_ = Cal(num)
  if cal<cal_:
    cal = cal_
    r = i
  num = Rot(num)
print(r)