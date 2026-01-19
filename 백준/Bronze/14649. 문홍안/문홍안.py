import sys
input = sys.stdin.readline

P = int(input().strip())
colors = [0] * 100
for _ in range(int(input().strip())):
    start, direction = input().split()
    if direction == 'R':
        for i in range(int(start), 100):
            colors[i] = (colors[i] + 1) % 3
    else:
        for i in range(0, int(start) - 1):
            colors[i] = (colors[i] + 1) % 3

a, b, c = colors.count(0), colors.count(1), colors.count(2)
print(f'{P * (a / 100):.2f}')
print(f'{P * (b / 100):.2f}')
print(f'{P * (c / 100):.2f}')