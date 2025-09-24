import sys
input = sys.stdin.readline

for _ in range(int(input())):
    C = list(map(int, input().split()))
    is_safe = True
    x_list, y_list = [], []
    for i in range(1, 2 * C[0], 2):
        x, y = C[i], C[i + 1]
        if x in x_list or y in y_list:
            is_safe = False
            break
        else:
            x_list.append(x)
            y_list.append(y)
    
    print('SAFE' if is_safe else 'NOT SAFE')