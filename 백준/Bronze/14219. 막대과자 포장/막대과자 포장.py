import sys
input = sys.stdin.readline

N, M = map(int, input().split())
if N % 3 != 0 and M % 3 != 0:
    print('NO')
else:
    print('YES')