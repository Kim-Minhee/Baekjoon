import math

for _ in range(int(input())):
  N, C = input().split()
  num = str(math.factorial(int(N)))
  print(num.count(C))