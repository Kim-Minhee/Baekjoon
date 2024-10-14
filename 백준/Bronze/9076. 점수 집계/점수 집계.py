for _ in range(int(input())):
  N = list(map(int, input().split()))
  N.sort()
  if N[3]-N[1]<4:
    print(sum(N[1:4]))
  else:
    print('KIN')