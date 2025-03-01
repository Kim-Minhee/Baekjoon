def earlier_time(time1, time2):
  if time1==time2:
    return 0

  h1, m1 = map(int, time1.split(':'))
  h2, m2 = map(int, time2.split(':'))
  if h1<h2 or (h1==h2 and m1<m2):
    return 1
  else:
    return 2


arrival_time = []
standard_time = ''

for _ in range(int(input())+1):
  T, R = input().split()
  if R=='student':
    arrival_time.append(T)
  else:
    standard_time = T
school_time = input()

if earlier_time(school_time, standard_time)==2:
  standard_time = school_time

cnt = 0
for time in arrival_time:
  if earlier_time(standard_time, time)<2:
    cnt += 1
print(cnt)