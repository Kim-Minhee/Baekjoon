import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
S = [0] + list(map(int, input().split()))
for _ in range(Q):
    DATA = list(map(int, input().split()))
    if DATA[0] == 1:
        a, b = DATA[1], DATA[2]
        print(sum(S[a:b + 1]))
        S[a], S[b] = S[b], S[a]
    else:
        a, b, c, d = DATA[1], DATA[2], DATA[3], DATA[4]
        print(sum(S[a:b + 1]) - sum(S[c:d + 1]))