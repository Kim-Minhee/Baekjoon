# GPT 5.1
import sys
input = sys.stdin.readline

def next_non_empty_line():
    """빈 줄을 건너뛰고, 내용이 있는 줄을 돌려준다."""
    while True:
        line = input()
        if not line:
            return ''  # EOF
        line = line.strip()
        if line != '':
            return line

T = int(next_non_empty_line())

for t in range(1, T + 1):
    # N 읽기
    N = int(next_non_empty_line())
    
    # 버스 구간들 읽기 (한 줄에 2N개 정수)
    ranges = list(map(int, next_non_empty_line().split()))
    
    MAX_CITY = 5000
    diff = [0] * (MAX_CITY + 2)  # B+1까지 접근하므로 +2

    # 차분 배열 처리
    for i in range(0, 2 * N, 2):
        A = ranges[i]
        B = ranges[i + 1]
        diff[A] += 1
        diff[B + 1] -= 1

    # prefix sum → 각 도시를 지나는 버스 개수
    for i in range(1, MAX_CITY + 1):
        diff[i] += diff[i - 1]

    # 관심 있는 도시 개수 P
    P = int(next_non_empty_line())

    result = []
    for _ in range(P):
        C = int(next_non_empty_line())
        result.append(str(diff[C]))

    print(f"Case #{t}: {' '.join(result)}")