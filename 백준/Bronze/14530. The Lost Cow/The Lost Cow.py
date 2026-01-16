import sys
input = sys.stdin.readline

X, Y = map(int, input().split())
total_dist = 0
current_x = X
dir = 0 # 짝수면 양의 방향, 홀수면 음의 방향
while True:
    if dir % 2 == 0:
        x = X + 2 ** dir
    else:
        x = X - 2 ** dir
    # print(x)
    if X <= Y <= x or x <= Y <= X:
        total_dist += abs(Y - current_x)
        break
    else:
        total_dist += abs(current_x - x)
        current_x = x
    dir += 1
print(total_dist)