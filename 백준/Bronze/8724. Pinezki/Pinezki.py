# Gemini 2.5 Pro
import sys

def solve_thumbtack_bridge():
    """
    압정이 놓인 다리를 건너기 위해 필요한 최소 점프 길이를 계산합니다.
    """
    try:
        # 첫 줄에서 다리의 길이 n을 읽어옵니다.
        n = int(sys.stdin.readline())
        # 두 번째 줄에서 다리의 상태를 리스트로 읽어옵니다.
        bridge_planks = list(map(int, sys.stdin.readline().split()))
    except (ValueError, IndexError):
        # 입력이 비었거나 형식이 잘못된 경우 종료합니다.
        return

    max_jump_needed = 0
    current_tack_sequence = 0

    # 다리의 각 판자를 순회합니다.
    for plank in bridge_planks:
        if plank == 1:
            # 압정(1)을 만나면, 현재 연속된 압정의 길이를 1 증가시킵니다.
            current_tack_sequence += 1
        else: # plank == 0
            # 안전한 발판(0)을 만나면, 지금까지의 연속 길이를 최대값과 비교합니다.
            if current_tack_sequence > max_jump_needed:
                max_jump_needed = current_tack_sequence
            # 현재 연속 길이를 0으로 초기화합니다.
            current_tack_sequence = 0

    # 루프가 끝난 후, 마지막에 연속된 압정 구간이 있었을 수 있으므로
    # 한 번 더 최대값을 비교하여 갱신합니다.
    if current_tack_sequence > max_jump_needed:
        max_jump_needed = current_tack_sequence

    # 최종적으로 계산된 최소 점프 길이를 출력합니다.
    print(max_jump_needed)

# 함수 실행
solve_thumbtack_bridge()