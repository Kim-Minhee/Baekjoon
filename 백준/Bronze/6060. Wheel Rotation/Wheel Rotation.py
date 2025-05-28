# Gemini
import sys

# 빠른 입력을 위해 sys.stdin.readline 사용 (선택 사항)
input = sys.stdin.readline

def solve_pulley_direction():
    """
    풀리의 회전 방향을 계산하고 출력하는 함수
    """
    try:
        # 풀리의 수 입력
        N_str = input().strip()
        if not N_str: # 빈 입력 처리
            return
        N = int(N_str)

        # 벨트 정보를 저장할 리스트
        belts = []
        for _ in range(N - 1):
            line = input().strip()
            if not line: # 빈 입력 처리
                continue
            # S_i (출발), D_i (도착), C_i (유형) 입력
            S_i, D_i, C_i = map(int, line.split())
            belts.append((S_i, D_i, C_i))

        # 벨트를 출발 풀리 번호(S_i) 기준으로 정렬합니다.
        # 이렇게 하면 풀리 1부터 순차적으로 연결을 따라갈 수 있습니다.
        belts.sort()

        # 초기 방향 설정 (풀리 1은 시계 방향 = 0)
        current_direction = 0

        # 정렬된 벨트를 순회하며 최종 방향을 추적합니다.
        for belt in belts:
            # 벨트의 연결 유형 (0: 직선, 1: 교차)
            connection_type = belt[2]

            # 교차 벨트(C_i = 1)를 만나면 방향을 전환합니다.
            if connection_type == 1:
                current_direction = 1 - current_direction  # 0이면 1로, 1이면 0으로 변경

        # 최종 풀리 N의 회전 방향을 출력합니다.
        print(current_direction)

    except Exception as e:
        print(f"An error occurred: {e}")

# 함수 호출
solve_pulley_direction()