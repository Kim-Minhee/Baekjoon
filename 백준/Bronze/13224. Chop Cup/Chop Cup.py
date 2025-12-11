import sys
input = sys.stdin.readline

MOVE = list(input().strip())
ball = [1, 0, 0]
for move in MOVE:
    if move == 'A':
        ball[0], ball[1] = ball[1], ball[0]
    elif move == 'B':
        ball[1], ball[2] = ball[2], ball[1]
    else:
        ball[0], ball[2] = ball[2], ball[0]
print(ball.index(1) + 1)