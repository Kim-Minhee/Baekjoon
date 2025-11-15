import sys
input = sys.stdin.readline

for _ in range(int(input().strip())):
    T = list(map(int, input().split()))
    non_birth_in_zanzibar = 0
    for i in range(len(T) - 2):
        able_cnt = T[i] * 2
        real_cnt = T[i + 1]
        if real_cnt > able_cnt:
            non_birth_in_zanzibar += real_cnt - able_cnt
    print(non_birth_in_zanzibar)