import sys
input = sys.stdin.readline

while True:
    try:
        D, VF, VG = map(int, input().split())
        time_thief = 12 / VF
        time_guard = ((144 + D ** 2) ** (1 /2)) / VG

        if time_thief >= time_guard:
            print('S')
        else:
            print('N')
    except:
        break