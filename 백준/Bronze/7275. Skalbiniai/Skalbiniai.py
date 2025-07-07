# Gemini 2.5 Pro
import sys

def solve_laundry_problem():
    """
    토마스가 모든 옷을 세탁하는 데 필요한 총 횟수를 계산합니다.
    """
    try:
        # 첫 줄에서 N, K, M을 읽어옵니다.
        N, K, M = map(int, sys.stdin.readline().split())
    except (ValueError, IndexError):
        return

    # K개의 그룹 정보를 저장할 리스트를 준비합니다.
    groups = []
    for _ in range(K):
        # 각 그룹의 정의를 읽어옵니다. 첫 숫자는 색상 개수이므로 제외하고,
        # 나머지 색상 번호들만 리스트로 만들어 groups에 추가합니다.
        group_info = list(map(int, sys.stdin.readline().split()))
        groups.append(group_info[1:])

    try:
        # N개의 색상별 옷 개수를 읽어옵니다.
        # 색상 번호가 1부터 시작하므로, 인덱스를 맞추기 위해 맨 앞에 0을 추가합니다.
        clothes_per_color = [0] + list(map(int, sys.stdin.readline().split()))
    except (ValueError, IndexError):
        return

    total_loads = 0
    # 각 그룹에 대해 필요한 세탁 횟수를 계산합니다.
    for group in groups:
        # 현재 그룹에 속한 모든 옷의 총 개수를 계산합니다.
        clothes_in_this_group = 0
        for color_index in group:
            clothes_in_this_group += clothes_per_color[color_index]
        
        # 현재 그룹의 세탁 횟수를 계산합니다 (올림 나눗셈).
        if clothes_in_this_group > 0:
            loads_for_this_group = (clothes_in_this_group + M - 1) // M
            total_loads += loads_for_this_group

    # 최종 결과를 출력합니다.
    print(total_loads)

# 함수 실행
solve_laundry_problem()