# GPT 5
import sys

for line in sys.stdin:
    N, T1, T2, T3 = map(int, line.split())
    if N == T1 == T2 == T3 == 0:
        break

    ccw = (T2 - T1) % N  # 반시계 거리
    cw  = (T2 - T3) % N  # 시계 거리
    ans = 4 * N - 1 + ccw + cw
    print(ans)