# GPT 5
import sys
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    m, n = map(int, input().split())
    tiles = list(map(int, input().split()))

    # 시작 위치와 방향 찾기
    start = tiles.index(2) if 2 in tiles else tiles.index(3)
    direction = 1 if 2 in tiles else -1

    pos = start
    yellow_count = 0

    for _ in range(n):
        next_pos = pos + direction
        # 벽에 닿으면 방향 전환
        if next_pos < 0 or next_pos >= m:
            direction *= -1
            next_pos = pos + direction
        pos = next_pos

        if tiles[pos] == 0:
            yellow_count += 1

    print(yellow_count)