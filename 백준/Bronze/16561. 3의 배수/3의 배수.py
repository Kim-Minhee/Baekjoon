import sys
input = sys.stdin.readline

N = int(input().strip())
if N < 9:
    print(0)
else:
    s = N // 3
    cnt = 0
    for a in range(1, s - 1):
        for b in range(1, s - a):
            cnt += 1
    print(cnt) 