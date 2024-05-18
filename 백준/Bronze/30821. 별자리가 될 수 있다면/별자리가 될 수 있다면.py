import math

N = int(input())
r = math.factorial(N)/(math.factorial(N-5)*math.factorial(5))
print(int(r))