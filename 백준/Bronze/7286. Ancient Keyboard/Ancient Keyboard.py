alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for _ in range(int(input())):
  N = int(input())
  pressed_time = []
  max_time = 0
  for _ in range(N):
    X, A, B = input().split()
    pressed_time.append((int(A), int(B)))
    if int(B)>max_time:
      max_time = int(B)
  
  pressed_key = [0]*(max_time+1)
  for start, end in pressed_time:
    for i in range(start, end):
      pressed_key[i] += 1

  printed = ''
  for key in pressed_key:
    if key!=0:
      printed += alphabet[key-1]
  
  print(printed)