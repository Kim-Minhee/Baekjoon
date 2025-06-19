# GPT 4o
C, R = map(int, input().split())
x, y = 0, 0

while True:
    dx, dy = map(int, input().split())
    if dx == 0 and dy == 0:
        break

    x = max(0, min(C, x + dx))
    y = max(0, min(R, y + dy))

    print(x, y)