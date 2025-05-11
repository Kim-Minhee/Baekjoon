while True:
  R = int(input())
  if R==0: break

  M = list(map(int, input().split()))
  L = list(map(int, input().split()))

  m = sum(M)
  l = sum(L)

  for i in range(2, R):
    if M[i-2]==M[i-1]==M[i] and L[i-2]==L[i-1]==L[i]:
      break
    elif M[i-2]==M[i-1]==M[i]:
      m += 30
      break
    elif L[i-2]==L[i-1]==L[i]:
      l += 30
      break

  if m>l:
    print('M')
  elif m<l:
    print('L')
  else:
    print('T')