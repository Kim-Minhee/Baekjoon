import sys

for i in range(int(sys.stdin.readline())):
  N = int(sys.stdin.readline())
  A, B = map(int, sys.stdin.readline().split())
  U, V = list(), list()
  for _ in range(N):
    Ui, Vi = map(int, sys.stdin.readline().split())
  print(f'Material Management {i+1}')
  print('Classification ---- End!')