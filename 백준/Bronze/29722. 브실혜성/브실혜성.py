def exp(num):
  if num<10:
    return '0'+str(num)
  else:
    return num

Y, M, D = map(int, input().split('-'))
N = int(input())
D += N
if D>30:
  if D%30!=0:
    M += D//30
    D = D%30
  else:
    M += D//30
    M -= 1
    D = 30
if M>12:
  if M%12!=0:
    Y += M//12
    M = M%12
  else:
    Y += M//12
    Y -= 1
    M = 12
M = exp(M)
D = exp(D)
print(Y, M, D, sep='-')