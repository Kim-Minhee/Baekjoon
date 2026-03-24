import sys
input = sys.stdin.readline

first, last = 1440, 0
for _ in range(int(input().strip())):
    H, M = map(int, input().split(':'))
    time = H * 60 + M
    if 390 <= time <= 1140:
        if time < first:
            first = time
        if time > last:
            last = time

if 390 <= first <= 600 and 390 <= last <= 960:
    print(24000)
elif 390 <= first <= 600 and 961 <= last <= 1140:
    print(36000)
elif 601 <= first <= 960 and 601 <= last <= 960:
    print(16800)
elif 601 <= first <= 1140 and 961 <= last <= 1140:
    print(24000)
else:
    print(0)