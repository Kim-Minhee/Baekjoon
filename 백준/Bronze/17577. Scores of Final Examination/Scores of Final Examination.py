# Gemini 3.1 Pro
import sys

def solve():
    # 입력을 빠르게 읽기 위해 모든 데이터를 한 번에 가져옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    idx = 0
    while idx < len(input_data):
        n = int(input_data[idx])      # 학생 수
        m = int(input_data[idx + 1])  # 과목 수
        idx += 2

        # 종료 조건: n과 m이 모두 0이면 반복 중단
        if n == 0 and m == 0:
            break

        # 각 학생의 총점을 저장할 리스트 (n명만큼 0으로 초기화)
        student_totals = [0] * n

        # m개의 과목에 대해 점수를 입력받아 누적
        for _ in range(m):
            for k in range(n):
                score = int(input_data[idx])
                student_totals[k] += score
                idx += 1

        # 이번 데이터셋에서 가장 높은 총점 출력
        print(max(student_totals))

if __name__ == '__main__':
    solve()