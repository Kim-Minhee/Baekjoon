import sys
input = sys.stdin.readline

N = int(input().strip())
while True:
    N += 1
    if '0' not in str(N):
        print(N)
        break