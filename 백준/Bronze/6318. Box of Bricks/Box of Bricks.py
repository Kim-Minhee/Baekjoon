i = 0
while True:
  N = int(input())
  if N==0: break
  i +=1

  H = list(map(int, input().split()))
  h_avg = sum(H)//N
  
  r = 0
  for h in H:
    if h>h_avg:
      r += h-h_avg
  
  print(f'Set #{i}')
  print(f'The minimum number of moves is {r}.')
  print()