# Gemini 2.5 Pro
import sys

def solve_combination_lock():
    """
    조합 자물쇠를 여는 데 필요한 최대 회전 눈금 수를 계산합니다.
    """
    # 0 0 0 0이 입력될 때까지 여러 테스트 케이스를 처리합니다.
    for line in sys.stdin:
        try:
            N, T1, T2, T3 = map(int, line.split())
        except (ValueError, IndexError):
            # 비어있는 줄이나 잘못된 입력은 건너뜁니다.
            continue

        # 종료 조건
        if N == 0 and T1 == 0 and T2 == 0 and T3 == 0:
            break

        # --- 수정된 계산 로직 ---

        # 1단계: 초기 위치를 최적화하여 얻을 수 있는 최대 회전 수
        # 2바퀴(2*N) + T1까지 가기 위한 최대 추가 회전(N-1)
        stage1_ticks = 2 * N + (N - 1)

        # 2단계: 반시계 방향 1바퀴 후, '시계 방향'으로 T2까지 이동
        # 1바퀴(N) + T1에서 T2까지의 '시계 방향' 거리
        stage2_ticks = N + (T2 - T1 + N) % N

        # 3단계: '반시계 방향'으로 T3까지 이동
        # T2에서 T3까지의 '반시계 방향' 거리
        stage3_ticks = (T2 - T3 + N) % N

        # 모든 단계의 회전 수를 더합니다.
        total_ticks = stage1_ticks + stage2_ticks + stage3_ticks
        
        print(total_ticks)

# 함수 실행
solve_combination_lock()