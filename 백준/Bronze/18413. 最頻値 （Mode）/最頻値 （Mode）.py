# Gemini 3.1 Pro
import sys
from collections import Counter

def solve():
    # 입력을 한 번에 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])
    A = list(map(int, input_data[2:]))

    # Counter를 사용하여 배열 A에 있는 각 숫자의 등장 횟수를 셉니다.
    counts = Counter(A)

    # 등장 횟수(values) 중 가장 큰 값을 출력합니다.
    print(max(counts.values()))

if __name__ == "__main__":
    solve()