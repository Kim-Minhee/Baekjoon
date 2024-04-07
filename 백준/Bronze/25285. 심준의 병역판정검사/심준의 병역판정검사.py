for _ in range(int(input())):
  H, W = map(float, input().split())
  bmi = W/((H/100)**2)
  if H<140.1:
    print(6)
  elif H<146:
    print(5)
  elif H<159:
    print(4)
  elif H<161:
    if bmi>=16 and bmi<35:
      print(3)
    else:
      print(4)
  elif H<204:
    if bmi>=20 and bmi<25:
      print(1)
    elif (bmi>=18.5 and bmi<20) or (bmi>=25 and bmi<30):
      print(2)
    elif (bmi>=16 and bmi<18.5) or (bmi>=30 and bmi<35):
      print(3)
    else:
      print(4)
  else:
    print(4)