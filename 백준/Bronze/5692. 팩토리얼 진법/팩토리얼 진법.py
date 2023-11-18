import sys, math

while 1:
  num, r = sys.stdin.readline().strip(), 0
  if num=='0':
    break
  for i, n in enumerate(num):
    r += int(n)*math.factorial(len(num)-i)
  print(r)