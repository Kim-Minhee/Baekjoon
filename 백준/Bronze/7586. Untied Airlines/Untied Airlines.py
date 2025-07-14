code_points = {'L':120, 'S':150, 'B':150, 'N':40,
               'C':160, 'D':100, 'R':100, 'O':100}

while True:
  PLAIN = input()
  if PLAIN=='#': break
  
  passengers = []
  points = []
  while True:
    LINE = input()
    if LINE=='00A': break
    seat, code = LINE.split()

    if seat[-1] not in 'ABCDEFGHIJ' or code not in code_points.keys():
      continue

    if seat not in passengers:
      passengers.append(seat)
      points.append(code_points[code])
    else:
      idx = passengers.index(seat)
      points[idx] += code_points[code]
  
  cnt = 0
  for point in points:
    if point>=200:
      cnt += 1
  
  print(PLAIN, cnt)