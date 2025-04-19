# GPT
while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break

    taro = [int(input()) for _ in range(N)]
    hanako = [int(input()) for _ in range(M)]

    sum_taro = sum(taro)
    sum_hanako = sum(hanako)
    diff = sum_taro - sum_hanako

    if diff % 2 != 0:
        print(-1)
        continue
    diff //= 2

    hanako_set = set(hanako)
    answer = None
    for t in taro:
        h = t - diff
        if h in hanako_set:
            if answer is None or t + h < sum(answer):
                answer = (t, h)

    if answer:
        print(*answer)
    else:
        print(-1)