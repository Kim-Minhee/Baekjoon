import sys

for _ in range(int(sys.stdin.readline())):
  L = list(map(int, sys.stdin.readline().split()))
  L.sort()
  print(L[2]**2+(L[0]+L[1])**2)