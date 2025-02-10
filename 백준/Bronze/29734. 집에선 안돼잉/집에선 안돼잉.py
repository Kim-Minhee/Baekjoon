N, M = map(int, input().split())
T, S = map(int, input().split())

zip_time = N
zip_time += (N//8)*S
if N%8==0:
  zip_time -= S

dok_time = M
dok_time += (M//8)*(2*T+S)
if M%8==0:
  dok_time -= (T+S)
else:
  dok_time += T

if zip_time<dok_time:
  print('Zip')
  print(zip_time)
else:
  print('Dok')
  print(dok_time)