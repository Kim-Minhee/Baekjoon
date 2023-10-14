num = list(map(int, input().split()))
num.sort()
a, b, c = num[0], num[1], num[2]
if (c-b)==(b-a):
  print(2*c-b)
elif 2*(c-b)==(b-a):
  print(2*b-c)
else:
  print(2*b-a)