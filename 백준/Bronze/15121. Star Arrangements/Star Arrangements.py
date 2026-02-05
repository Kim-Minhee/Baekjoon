import sys
input = sys.stdin.readline

S = int(input().strip())
print(f'{S}:')
for x in range(2, S // 2 + 2):
    for y in range(x - 1, x + 1):
        one_set = x + y
        if S % one_set == 0 or S % one_set == x:
            print(f'{x},{y}')