# GPT 5.1
import sys
input = sys.stdin.readline

T = int(input().strip())

for t in range(1, T + 1):

    # blank line이 있을 수도 있고 없을 수도 있으므로 처리
    line = input().strip()
    while line == "":              # 빈 줄이면 계속 넘김
        line = input().strip()
    N = int(line)

    # N개의 버스 범위 입력
    data = list(map(int, input().split()))
    buses = []
    for i in range(0, 2 * N, 2):
        A = data[i]
        B = data[i + 1]
        buses.append((A, B))

    # 질의 개수 P
    P = int(input().strip())
    queries = [int(input().strip()) for _ in range(P)]

    # 각 도시별 버스 카운트
    result = []
    for city in queries:
        cnt = 0
        for A, B in buses:
            if A <= city <= B:
                cnt += 1
        result.append(cnt)

    print(f"Case #{t}: {' '.join(map(str, result))}")