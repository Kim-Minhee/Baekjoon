# GPT
while True:
    N = int(input())
    if N == 0:
        break

    lotto_set = set()

    for _ in range(N):
        ticket = map(int, input().split())
        lotto_set.update(ticket)

    print('Yes' if len(lotto_set)==49 else 'No')