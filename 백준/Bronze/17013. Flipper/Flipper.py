# GPT 5
import sys
input = sys.stdin.readline

S = input().strip()

h = S.count('H') % 2
v = S.count('V') % 2

# 초기 상태
grid = [[1, 2], [3, 4]]

# H 적용
if h == 1:
    grid[0], grid[1] = grid[1], grid[0]

# V 적용
if v == 1:
    grid[0][0], grid[0][1] = grid[0][1], grid[0][0]
    grid[1][0], grid[1][1] = grid[1][1], grid[1][0]

# 출력
for row in grid:
    print(*row)