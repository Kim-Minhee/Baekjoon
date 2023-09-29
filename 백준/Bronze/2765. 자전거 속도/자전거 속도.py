n = 1
while True:
  r, c, t = map(float, input().split())
  if c==0:
    break
  r /= 12
  r /= 5280
  t /= 60
  t /= 60
  distance = 3.1415927*r*c
  mph = distance/t
  print(f'Trip #{n}: {round(distance, 2):.2f} {round(mph, 2):.2f}')
  n += 1