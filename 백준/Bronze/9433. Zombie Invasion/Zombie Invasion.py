for _ in range(int(input())):
    VILLAGERS = list(map(int, input().split()))

    for i in range(19, 0, -1):
        villager = VILLAGERS[i]
        VILLAGERS[i] = 0 if villager % 2 == 0 else 1
        VILLAGERS[i-1] += villager // 2

    print(*VILLAGERS)