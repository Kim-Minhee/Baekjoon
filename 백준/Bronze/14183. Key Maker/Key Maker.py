import sys
input = sys.stdin.readline

while True:
    M, N = map(int, input().split())
    if M == N == 0:
        break

    C = list(map(int, input().split()))
    possible_cnt = 0
    for _ in range(N):
        S = list(map(int, input().split()))
        for idx, depth in enumerate(S):
            if C[idx] < depth:
                break
        else:
            possible_cnt += 1
    print(possible_cnt)