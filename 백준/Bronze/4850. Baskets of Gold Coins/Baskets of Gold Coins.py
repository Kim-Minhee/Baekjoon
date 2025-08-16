while True:
    try:
        N, W, D, M = map(int, input().split())

        golden_cnt = (N * (N - 1)) // 2
        golden_weight = W * golden_cnt
        if golden_weight == M:
            print(N)
        else:
            r = (golden_weight - M) // D
            print(r)
    except:
        break