for _ in range(int(input())):
    N, K = map(int, input().split())
    r = (N - K) // (K - 1)
    print(r)