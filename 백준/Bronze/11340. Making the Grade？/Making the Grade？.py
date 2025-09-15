# GPT 5
import sys
import math

input = sys.stdin.readline
T = int(input().strip())
for _ in range(T):
    p, paper, mid = map(int, input().split())
    base = 15*p + 20*paper + 25*mid  # 100분율로 환산한 부분합
    need = 9000 - base
    if need <= 0:
        print(0)
    else:
        # 올림(ceil) 정수로 계산
        final_needed = (need + 39) // 40  # (need + 40 - 1) // 40
        if final_needed > 100:
            print("impossible")
        else:
            print(final_needed)