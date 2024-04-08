for _ in range(int(input())):
  Y, M = map(int, input().split())
  if M==1:
    print(Y-1, 12, 31)
  elif M in [2, 4, 6, 8, 9, 11]:
    print(Y, M-1, 31)
  elif M in [5, 7, 10, 12]:
    print(Y, M-1, 30)
  elif (Y%100!=0 and Y%4==0) or Y%400==0:
    print(Y, 2, 29)
  else:
    print(Y, 2, 28)