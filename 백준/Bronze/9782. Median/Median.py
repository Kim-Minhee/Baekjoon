i = 0
while True:
  i += 1
  data = list(map(int, input().split()))
  if data==[0]:
    break
  else:
    n = len(data)-1
    if n%2==0:
      r = (data[n//2]+data[n//2+1])/2
      print(f'Case {i}: {r:.1f}')
    else:
      r = data[(n+1)//2]
      print(f'Case {i}: {r:.1f}')