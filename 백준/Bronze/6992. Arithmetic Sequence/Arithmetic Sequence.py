for _ in range(int(input())):
  N = list(map(int, input().split()))
  
  chk =  True
  d = N[2] - N[1]
  for i in range(3, len(N)):
    if d!=(N[i]-N[i-1]):
      chk = False
      break
  
  if chk:
    for j in range(5):
      N.append(N[-1]+d)
    print(f'The next 5 numbers after {N[1:-5]} are: {N[-5:]}')
  else:
    print(f'The sequence {N[1:]} is not an arithmetic sequence.')