# Gemini 2.5 Pro
import sys

def solve_attention_level():
    """
    교실의 전체 집중도를 계산하는 문제를 해결합니다.
    """
    try:
        # 첫 줄에서 행(M)과 열(N)의 개수를 읽어옵니다.
        M, N = map(int, sys.stdin.readline().split())
    except (ValueError, IndexError):
        # 잘못된 입력의 경우 종료합니다.
        return

    # M개의 줄을 읽어 격자를 정수형 2차원 리스트로 저장합니다.
    grid = []
    for _ in range(M):
        # 각 줄을 읽어 문자 하나하나를 정수로 변환하여 리스트로 만듭니다.
        row = [int(char) for char in sys.stdin.readline().strip()]
        grid.append(row)

    total_attention = 0.0

    # 각 학생(셀)을 순회합니다.
    for r in range(M):
        for c in range(N):
            current_student_interest = grid[r][c]
            sum_of_differences = 0
            neighbor_count = 0

            # 상, 하, 좌, 우 네 방향의 이웃을 확인합니다.
            # dr, dc는 (행, 열)의 변화량을 나타냅니다.
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc

                # 이웃이 격자 범위 내에 있는지 확인합니다.
                if 0 <= nr < M and 0 <= nc < N:
                    neighbor_interest = grid[nr][nc]
                    # 현재 학생과 이웃 학생의 관심도 차이의 절댓값을 더합니다.
                    sum_of_differences += abs(current_student_interest - neighbor_interest)
                    neighbor_count += 1
            
            # 한 학생의 집중도를 계산합니다 (이웃이 있는 경우에만).
            if neighbor_count > 0:
                individual_attention = sum_of_differences / neighbor_count
                total_attention += individual_attention

    # 최종 결과를 소수점 아래 4자리까지 형식에 맞춰 출력합니다.
    print(f"{total_attention:.4f}")

# 함수 실행
solve_attention_level()