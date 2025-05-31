# GPT 4o
i = 0
while True:
  N = int(input())
  if N==0: break
  i +=1

  H = list(map(int, input().split()))
  h_avg = sum(H)//N
  
  r = sum(h - h_avg for h in H if h > h_avg)
  
  print(f'Set #{i}')
  print(f'The minimum number of moves is {r}.')
  print()