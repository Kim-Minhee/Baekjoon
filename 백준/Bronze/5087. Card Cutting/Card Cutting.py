while True:
  CARD = input().split()
  if CARD==['#']: break

  cheryl, tania = 0, 0
  for num in CARD[:-1]:
    if num=='A':
      num = '1'
    if int(num)%2==0:
      tania += 1
    else:
      cheryl += 1
  
  if cheryl>tania:
    print('Cheryl')
  elif cheryl<tania:
    print('Tania')
  else:
    print('Draw')