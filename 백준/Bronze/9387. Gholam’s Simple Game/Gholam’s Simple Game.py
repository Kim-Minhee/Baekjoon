import sys
input = sys.stdin.readline

for _ in range(int(input().strip())):
    M, N = map(int, input().split())
    A = list(map(int, input().split()))
    if 2 in A:
        current = A.index(2) + 1
        dir = 1
    else:
        current = A.index(3) + 1
        dir = -1
    
    cnt_y = 0
    for _ in range(N):
        if dir == 1 and current == M:
            dir = -1
        elif dir == -1 and current == 1:
            dir = 1
        current += dir
        if A[current - 1] == 0:
            cnt_y += 1
    print(cnt_y)