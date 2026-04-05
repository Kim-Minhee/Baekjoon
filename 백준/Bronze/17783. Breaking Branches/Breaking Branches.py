import sys
input = sys.stdin.readline

N = int(input().strip())
if N % 2 == 0:
    print('Alice')
    print(1)
else:
    print('Bob')