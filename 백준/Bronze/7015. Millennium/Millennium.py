millennium = 0
for year in range(1, 1000):
  if year%3==0:
    millennium += 200
  else:
    millennium += 195

for _ in range(int(input())):
  Y, M, D = map(int, input().split())

  days = 0
  for y in range(1, Y):
    if y%3==0:
      days += 200
    else:
      days += 195
  for m in range(1, M):
    if Y%3!=0 and m%2==0:
      days += 19
    else:
      days += 20
  days += D
        
  print(millennium - days + 1)