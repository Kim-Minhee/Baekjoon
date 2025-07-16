while True:
  PLAIN, N = input().split()
  if PLAIN=='#' and N=='0': break
  
  booking = int(N)
  while True:
    TYPE, S = input().split()
    if TYPE=='X' and S=='0': break

    s = int(S)
    if TYPE=='B' and s<=68-booking:
      booking += s
    elif TYPE=='C' and s<=booking:
      booking -= s
    
  print(PLAIN, booking)