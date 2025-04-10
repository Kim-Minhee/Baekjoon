# GPT
while True:
    N = int(input())
    if N == 0:
        break

    n = 1
    while n*(n+1)//2 < N:
        n += 1

    used_days = (n-1)*n//2
    total_coins = (n-1)*n*(2*n-1)//6  # 1^2 + 2^2 + ... + (n-1)^2
    total_coins += (N-used_days)*n

    print(N, total_coins)