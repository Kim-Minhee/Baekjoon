import math

while True:
  line = input()
  if not line: continue
  
  N = int(line)
  if N==0: break

  num = str(math.factorial(N))

  num_dict = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
  for n in num:
    num_dict[n] += 1
  
  r = []
  for i in range(10):
    cnt = num_dict[str(i)]
    r.append(' '*(5-len(str(cnt))) + str(cnt))

  print(f'{N}! --')
  print(f'   (0){r[0]}    (1){r[1]}    (2){r[2]}    (3){r[3]}    (4){r[4]} ')
  print(f'   (5){r[5]}    (6){r[6]}    (7){r[7]}    (8){r[8]}    (9){r[9]} ')