a, b, c, d = map(int, input().split())
time = list(map(int, input().split()))
att = [0, 0, 0]
for i, v in enumerate(time):
  if v%(a+b)>0 and v%(a+b)<=a:
    att[i] += 1
  if v%(c+d)>0 and v%(c+d)<=c:
    att[i] += 1
for i in att:
  print(i)