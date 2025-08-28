import sys
input = sys.stdin.readline

for _ in range(int(input())):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A = set(A[1:])
    A = list(A)
    A.sort()
    B = set(B[1:])
    B = list(B)
    B.sort()
    
    min_diff = 1000000
    for a in A:
        for b in B:
            diff = abs(a - b)
            min_diff = min(min_diff, diff)
        if min_diff == 0:
            break
    
    print(min_diff)