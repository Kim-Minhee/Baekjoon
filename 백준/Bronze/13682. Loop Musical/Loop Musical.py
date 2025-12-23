# GPT 5.2
import sys
input = sys.stdin.readline

while True:
    N = int(input().strip())
    if N == 0:
        break

    H = list(map(int, input().split()))
    peaks = 0

    for i in range(N):
        prev = H[i-1]            # i=0이면 H[-1] → 마지막 (루프)
        curr = H[i]
        nxt  = H[(i+1) % N]      # 다음도 루프 처리

        # 국소 최대 또는 국소 최소
        if (curr > prev and curr > nxt) or (curr < prev and curr < nxt):
            peaks += 1

    print(peaks)