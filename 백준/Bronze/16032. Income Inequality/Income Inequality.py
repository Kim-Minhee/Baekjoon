import sys
input = sys.stdin.readline

while True:
    N = int(input().strip())
    if N == 0:
        break
    A = list(map(int, input().split()))
    A.sort()
    avg = sum(A) / N
    print(sum(1 for a in A if a <= avg))