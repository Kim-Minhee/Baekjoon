import sys
input = sys.stdin.readline

for _ in range(int(input().strip())):
    Y = list(map(int, input().split(',')))
    r = [y for y in Y if y % 4 == 0]
    print(*r)