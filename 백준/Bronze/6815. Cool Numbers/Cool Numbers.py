A, B = int(input()), int(input())

square_list = []
i = 1
while True:
  if i**2>=A and i**2<=B:
    square_list.append(i**2)
  elif i**2>B:
    break
  i += 1

cube_cnt = 0
j = 1
while True:
  if j**3 in square_list:
    cube_cnt += 1
  if j**3>B:
    break
  j += 1

print(cube_cnt)