i = 0
while True:
  N = int(input())
  if N==0:
    break
  
  A = list(map(int, input().split()))
  B = list(map(int, input().split()))

  a_score, b_score = 0, 0
  for n in range(N):
    a, b = A[n], B[n]
    if a==1 and b==2:
      a_score += 6
    elif a==2 and b==1:
      b_score += 6
    elif b-a==1:
      a_score += a+b
    elif a-b==1:
      b_score += a+b
    elif a>b:
      a_score += a
    elif a<b:
      b_score += b

  if i!=0:
    print()
  print(f'A has {a_score} points. B has {b_score} points.')

  i += 1