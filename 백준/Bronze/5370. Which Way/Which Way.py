try:
  while True:
    N = int(input())
    b = bin(N)[2:]

    cnt_0 = b.count('0')
    cnt_1 = b.count('1')
    if cnt_0>cnt_1:
      print('left')
    elif cnt_0==cnt_1:
      print('straight')
    else:
      print('right')
except:
  exit()