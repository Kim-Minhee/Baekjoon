N = int(input())

if N<5:
  for _ in range(N):
    print('*'*N)
else:
  stars = ['*'*N]
  for i in range((N-2)//2):
    star = [' ']*N
    star[0], star[-1] = '*', '*'
    star[i+1], star[-i-2] = '*', '*'
    stars.append(''.join(star))
  if N%2==0:
    for s in stars:
      print(s)
    for s in stars[::-1]:
      print(s)
  else:
    star = [' ']*N
    star[0], star[-1], star[N//2] = '*', '*', '*'
    stars.append(''.join(star))
    for s in stars:
      print(s)
    for s in stars[-2::-1]:
      print(s)