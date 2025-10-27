import sys
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))

chk = True
for i in range(N - 1):
    if A[i + 1] - A[i] < 0:
        chk = False
        break
print('yes' if chk else 'no')