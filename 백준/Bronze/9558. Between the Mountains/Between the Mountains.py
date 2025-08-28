import sys
input = sys.stdin.readline

for _ in range(int(input())):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    min_diff = 1000000
    for a in set(A[1:]):
        for b in set(B[1:]):
            diff = abs(a - b)
            min_diff = min(min_diff, diff)
        if min_diff == 0:
            break
    
    print(min_diff)