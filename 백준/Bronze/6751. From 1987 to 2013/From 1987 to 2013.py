Y = int(input())

while True:
  Y += 1
  if len(set(str(Y)))==len(list(str(Y))):
    print(Y)
    break