def distance(total, forward, backward):
  pair = forward + backward
  dist_dif = forward - backward
  dist = total // pair * dist_dif

  mod = total % pair
  if mod > forward:
    dist += 2 * forward - mod
  elif mod > 0:
    dist += mod

  return dist

A, B = int(input()), int(input())
C, D = int(input()), int(input())
S = int(input())

nikky = distance(S, A, B)
byron = distance(S, C, D)

if nikky>byron:
  print('Nikky')
elif nikky<byron:
  print('Byron')
else:
  print('Tied')