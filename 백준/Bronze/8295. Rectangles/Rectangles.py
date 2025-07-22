# Gemini 2.5 Pro
import sys

def solve_rectangle_counting():
    """
    n x m 격자에서 둘레가 p 이상인 직사각형의 개수를 계산합니다.
    """
    try:
        # 한 줄을 읽어와서 n, m, p로 분리합니다.
        n, m, p = map(int, sys.stdin.readline().split())
    except (ValueError, IndexError):
        # 입력이 비었거나 형식이 잘못된 경우 종료합니다.
        return

    total_count = 0

    # 1부터 n까지 모든 가능한 세로 길이(h)를 순회합니다.
    for h in range(1, n + 1):
        # 1부터 m까지 모든 가능한 가로 길이(w)를 순회합니다.
        for w in range(1, m + 1):
            # 현재 h x w 크기 직사각형의 둘레를 계산합니다.
            perimeter = 2 * (h + w)

            # 둘레가 최소 조건 p 이상인지 확인합니다.
            if perimeter >= p:
                # 조건을 만족하면, 이 크기의 직사각형이 격자 내에
                # 몇 개나 존재할 수 있는지 계산하여 더합니다.
                
                # 세로로 가능한 위치의 수
                possible_vertical_placements = n - h + 1
                # 가로로 가능한 위치의 수
                possible_horizontal_placements = m - w + 1
                
                count_for_this_size = possible_vertical_placements * possible_horizontal_placements
                total_count += count_for_this_size

    # 최종적으로 계산된 총 개수를 출력합니다.
    print(total_count)

# 함수 실행
solve_rectangle_counting()