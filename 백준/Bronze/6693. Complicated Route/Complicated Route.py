def split_num_str(num_str):
  for i in range(len(num_str)):
    if not num_str[i].isdigit():
      return int(num_str[:i]), num_str[i:]

while True:
  D = input()
  if D=='END': break
  
  current_x, current_y = 0, 0
  for d in D[:-1].split(','):
    step, dir = split_num_str(d)
    if dir=='N':
      current_y += step
    elif dir=='E':
      current_x += step
    elif dir=='S':
      current_y -= step
    elif dir=='W':
      current_x -= step
    else:
      a = ((step**2)/2)**(1/2)
      if dir=='NE':
        current_x += a
        current_y += a
      elif dir=='SE':
        current_x += a
        current_y -= a
      elif dir=='SW':
        current_x -= a
        current_y -= a
      elif dir=='NW':
        current_x -= a
        current_y += a
    
  dist = (current_x**2+current_y**2)**(1/2)
  print(f'You can go to ({current_x:.3f},{current_y:.3f}), the distance is {dist:.3f} steps.')