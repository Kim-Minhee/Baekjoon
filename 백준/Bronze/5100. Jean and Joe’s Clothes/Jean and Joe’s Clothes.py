while True:
  N = int(input())
  if N==0: break

  joe, jean, jane, james, unknown = 0, 0, 0, 0, 0
  for _ in range(N):
    SIZE = input()
    if SIZE=='M' or SIZE=='L':
      joe += 1
    elif SIZE=='S':
      james += 1
    elif SIZE=='X':
      unknown += 1
    elif int(SIZE)>=12:
      jean += 1
    else:
      jane += 1
  print(joe, jean, jane, james, unknown)