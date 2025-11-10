import sys
input = sys.stdin.readline

R, Y, B = map(int, input().split())
P = [int(input().strip()) for _ in range(6)]
need_red = max(round((P[3] + P[5]) / 2 + P[4] - R, 1), 0)
need_yellow = max(round((P[1] + P[5]) / 2 + P[0] - Y, 1), 0)
need_blue = max(round((P[1] + P[3]) / 2 + P[2] - B, 1), 0)
if need_red % 1 == 0:
    need_red = int(need_red)
if need_yellow % 1 == 0:
    need_yellow = int(need_yellow)
if need_blue % 1 == 0:
    need_blue = int(need_blue)
print(f'{need_red} {need_yellow} {need_blue}')