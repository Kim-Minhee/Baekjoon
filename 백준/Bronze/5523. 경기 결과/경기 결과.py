import sys

cnt_a = cnt_b = 0
for _ in range(int(sys.stdin.readline())):
  a, b = map(int, sys.stdin.readline().split())
  if a>b:
    cnt_a += 1
  elif b>a:
    cnt_b += 1
print(cnt_a, cnt_b)