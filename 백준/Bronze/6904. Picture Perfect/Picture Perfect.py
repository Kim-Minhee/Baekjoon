while True:
  C = int(input())
  if C==0: break
  
  for a in range(int(C**(1/2)), C+1): 
    if C%a==0:
      b = C//a
      print(f'Minimum perimeter is {2*(a+b)} with dimensions {min(a, b)} x {max(a, b)}')
      break