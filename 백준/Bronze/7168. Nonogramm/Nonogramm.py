# GPT 4o
def count_blocks(line):
    counts = []
    count = 0
    for ch in line:
        if ch == '#':
            count += 1
        else:
            if count > 0:
                counts.append(count)
                count = 0
    if count > 0:
        counts.append(count)
    return counts if counts else [0]

# 입력
N, M = map(int, input().split())
grid = [input().strip() for _ in range(N)]

# 행 정보
for row in grid:
    print(' '.join(map(str, count_blocks(row))))

# 열 정보
for col in range(M):
    column = [grid[row][col] for row in range(N)]
    print(' '.join(map(str, count_blocks(column))))