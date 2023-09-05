import sys
n, t = int(sys.stdin.readline().rstrip()), 1
for _ in range(n):
  p = int(sys.stdin.readline().rstrip())
  t -= 1
  t += p
print(t)