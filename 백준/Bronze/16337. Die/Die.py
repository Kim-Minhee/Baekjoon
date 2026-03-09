# GPT 5
import sys

grid = [list(sys.stdin.readline().strip()) for _ in range(3)]

def rotate(g):
    return [list(row) for row in zip(*g[::-1])]

patterns = {
    1: {(1,1)},
    2: {(0,0),(2,2)},
    3: {(0,0),(1,1),(2,2)},
    4: {(0,0),(0,2),(2,0),(2,2)},
    5: {(0,0),(0,2),(1,1),(2,0),(2,2)},
    6: {(0,0),(1,0),(2,0),(0,2),(1,2),(2,2)}
}

for _ in range(4):
    pos = {(i,j) for i in range(3) for j in range(3) if grid[i][j] == 'o'}
    
    for num, p in patterns.items():
        if pos == p:
            print(num)
            sys.exit(0)
    
    grid = rotate(grid)

print("unknown")