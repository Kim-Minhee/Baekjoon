import sys
input = sys.stdin.readline

N = int(input().strip())
chk = True
a, b = map(int, input().split())
for _ in range(N - 1):
    A, B = map(int, input().split())
    if a < A:
        a = A
    if b > B:
        b = B
    if a > b:
        chk = False
if chk:
    print('gunilla has a point')
else:
    print('edward is right')