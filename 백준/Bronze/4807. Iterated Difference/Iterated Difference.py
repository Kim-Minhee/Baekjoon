i = 1
while True:
  N = int(input())
  if N==0: break

  lst = list(map(int, input().split()))

  chk = True
  iter = 0
  while len(set(lst))!=1:
    iter += 1

    new_lst = []
    for index in range(N):
      if index!=N-1:
        new_lst.append(abs(lst[index]-lst[index+1]))
      else:
        new_lst.append(abs(lst[index]-lst[0]))

    if iter>1000:
      chk = False
      break
    else:
      lst = new_lst


  if chk:
    print(f'Case {i}: {iter} iterations')
  else:
    print(f'Case {i}: not attained')

  i += 1