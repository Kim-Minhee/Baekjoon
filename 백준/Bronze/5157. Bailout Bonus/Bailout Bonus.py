# GPT
K = int(input())
for k in range(1, K+1):
    C, B, N, R = map(int, input().split())
    B_SET = set(map(int, input().split()))
    total_tax = 0

    for _ in range(N):
        c, p = map(int, input().split())
        if c in B_SET:
            total_tax += (p * R) // 100

    if k != 1:
        print()
    print(f'Data Set {k}:')
    print(total_tax)