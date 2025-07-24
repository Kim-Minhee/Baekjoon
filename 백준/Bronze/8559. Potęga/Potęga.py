N = int(input())

r_list = [2, 4, 8, 6]
if N==0:
  print(1)
else:
  print(r_list[N%4-1])