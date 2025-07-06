def time(h, m):
  return h*60+m

time_start = time(9, 0)
time_end = time(20, 59)

for _ in range(int(input())):
  H_S, M_S, H_E, M_E = map(int, input().split())
  start = time(H_S, M_S)
  end = time(H_E, M_E)
  
  time_start = max(time_start, start)
  time_end = min(time_end, end)
if time_start<time_end:
  print('TAIP')
  print(time_start//60, time_start%60, time_end//60, time_end%60)
else:
  print('NE')