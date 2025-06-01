import math

N, K = map(int, input().split())
for _ in range(K):
  S, T, R = map(int, input().split())

  reading_time = math.ceil(N/S)
  reading_time += (reading_time//T)*R if reading_time%T!=0 else (reading_time//T-1)*R

  print(reading_time)