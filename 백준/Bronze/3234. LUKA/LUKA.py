X, Y = (map(int, input().split()))
K = int(input())
M = input()

luka = {
    (X-1, Y+1), (X, Y+1), (X+1, Y+1),
    (X-1, Y), (X, Y), (X+1, Y),
    (X-1, Y-1), (X, Y-1), (X+1, Y-1)
}

ttm_x, ttm_y = 0, 0
time = []

if (ttm_x, ttm_y) in luka:
    time.append(0)

direction = {
    'I': (1, 0),
    'S': (0, 1),
    'Z': (-1, 0),
    'J': (0, -1)
}

for i, move in enumerate(M):
    dx, dy = direction[move]
    ttm_x += dx
    ttm_y += dy

    if (ttm_x, ttm_y) in luka:
        time.append(i+1)

if not time:
    print(-1)
else:
    print('\n'.join(map(str, time)))