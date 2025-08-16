# GPT 5
import sys

for line in sys.stdin:
    if not line.strip():
        continue
    N, w, d, measured = map(int, line.split())
    S = (N - 1) * N // 2  # 총 코인 개수
    ideal = S * w         # 전부 정상 무게라면
    diff = (ideal - measured) // d
    if diff == 0:
        print(N)
    else:
        print(diff)