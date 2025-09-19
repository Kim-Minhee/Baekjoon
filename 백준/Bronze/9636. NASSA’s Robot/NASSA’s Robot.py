import sys
input = sys.stdin.readline

for _ in range(int(input())):
    D = input()

    current_x, current_y = 0, 0
    for d in D:
        if d == '?':
            continue
        elif d == 'U':
            current_y += 1
        elif d == 'R':
            current_x += 1
        elif d == 'D':
            current_y -= 1
        elif d == 'L':
            current_x -= 1
    
    if '?' not in D:
        print(current_x, current_y, current_x, current_y)
    else:
        cnt = D.count('?')
        min_x = current_x - cnt
        min_y = current_y - cnt
        max_x = current_x + cnt
        max_y = current_y + cnt
        print(min_x, min_y, max_x, max_y)