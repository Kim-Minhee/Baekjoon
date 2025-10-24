# Gemini 2.5 Pro
import sys

def solve():
    """
    도시 A에서 도시 B로 가는 가장 저렴한 단일 항공 노선의 비용을 찾습니다.
    """
    try:
        # 출발 도시 A, 도착 도시 B, 노선 수 N을 읽습니다.
        a, b, n = map(int, sys.stdin.readline().split())

        # 최소 비용을 저장할 변수, 초기값은 매우 큰 값으로 설정합니다.
        min_cost = float('inf')

        # N개의 노선을 하나씩 확인합니다.
        for _ in range(n):
            # 노선 비용과 도시 수를 읽습니다.
            cost, num_cities = map(int, sys.stdin.readline().split())
            # 노선상의 도시 목록을 읽습니다.
            cities_on_route = list(map(int, sys.stdin.readline().split()))

            # 1. 도시 A와 B가 모두 노선에 포함되어 있는지 확인합니다.
            if a in cities_on_route and b in cities_on_route:
                # 2. A와 B의 위치(인덱스)를 찾습니다.
                index_a = -1
                index_b = -1
                for i in range(len(cities_on_route)):
                    if cities_on_route[i] == a:
                        index_a = i
                    if cities_on_route[i] == b:
                        index_b = i
                    # 두 인덱스를 모두 찾았으면 더 이상 탐색할 필요가 없습니다.
                    if index_a != -1 and index_b != -1:
                         break # 현재 노선의 도시 목록 탐색 중단

                # 3. 도시 A가 도시 B보다 먼저 나오는지 확인합니다.
                if index_a < index_b:
                    # 조건을 만족하면, 현재 노선 비용과 기록된 최소 비용을 비교하여 갱신합니다.
                    if cost < min_cost:
                        min_cost = cost

        # 모든 노선을 확인한 후 결과를 출력합니다.
        if min_cost == float('inf'):
            # 조건을 만족하는 노선이 하나도 없었던 경우
            print(-1)
        else:
            # 찾은 최소 비용 출력
            print(min_cost)

    except (ValueError, IndexError):
        # 입력이 잘못된 경우를 대비한 예외 처리입니다.
        pass

# 메인 함수 실행
solve()