import sys
input = sys.stdin.readline

num = '123456789'
for _ in range(int(input().strip())):
    CAR = input().strip()
    if CAR[0] != CAR[1] or CAR[0] not in num:
        continue
    if CAR[2] not in num or CAR[3] not in num:
        continue
    if not ('A' <= CAR[4] <= 'Z'):
        continue
    if CAR[5] not in num or CAR[6] not in num or CAR[7] not in num:
        continue
    print(CAR)