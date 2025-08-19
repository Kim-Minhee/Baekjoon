# Gemini 2.5 Pro
import sys

def solve_bed_bug_placement():
    """
    N개의 칸에 K마리의 벌레를 놓아 연속된 두 벌레 사이의
    최소 빈 칸 수를 최대화하는 문제를 해결합니다.
    """
    try:
        # 첫 줄에서 테스트 케이스의 수를 읽어옵니다.
        num_test_cases = int(sys.stdin.readline())
    except (ValueError, IndexError):
        return

    # 각 테스트 케이스에 대해 반복합니다.
    for _ in range(num_test_cases):
        try:
            # 한 줄을 읽어와서 N과 K로 분리합니다.
            N, K = map(int, sys.stdin.readline().split())
        except (ValueError, IndexError):
            continue

        # 벌레를 제외한 순수한 빈 칸의 총 개수를 계산합니다.
        total_empty_cells = N - K

        # 벌레들 사이의 공간(gap)의 수를 계산합니다.
        num_gaps = K - 1

        # 빈 칸들을 각 공간에 균등하게 분배한 값이
        # 최대화된 최소 거리가 됩니다.
        maximized_min_distance = total_empty_cells // num_gaps

        # 최종 결과를 출력합니다.
        print(maximized_min_distance)

# 함수 실행
solve_bed_bug_placement()