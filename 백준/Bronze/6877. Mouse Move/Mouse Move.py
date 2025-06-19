C, R = map(int, input().split())

current_x, current_y = 0, 0
while True:
  X, Y = map(int, input().split())
  if X==Y==0: break

  current_x += X
  if current_x<0: current_x = 0
  elif current_x>C: current_x = C

  current_y += Y
  if current_y<0: current_y = 0
  elif current_y>R: current_y = R

  print(current_x, current_y)