import sys
input = sys.stdin.readline

one_hole = 'ADOPQR'
for _ in range(int(input().strip())):
    total_holes = 0
    for ch in input().strip():
        if ch == 'B':
            total_holes += 2
        elif ch in one_hole:
            total_holes += 1
    print(total_holes)