import sys

bars = []
for _ in range(int(sys.stdin.readline())):
  bars.append(int(sys.stdin.readline()))

cnt, m = 0, 0
for i, h in enumerate(bars[::-1]):
  if i==0 or h>m:
    cnt += 1
    m = h

print(cnt)