import sys
input = sys.stdin.readline

def traffic_jam(time):
    if 7 * 60 <= time < 10 * 60 or 15 * 60 <= time < 19 * 60:
        return True
    return False

H, M = map(int, input().strip().split(':'))
time = H * 60 + M
dist = 240
while dist > 0:
    if traffic_jam(time):
        dist -= 1
    else:
        dist -= 2
    time += 1
h = str((time // 60) % 24).zfill(2)
m = str(time % 60).zfill(2)
print(f'{h}:{m}')