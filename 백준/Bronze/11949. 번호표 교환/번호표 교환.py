# Gemini 2.5 Pro
import sys
# sys.stdin.readline을 input 함수로 정의하여 입력을 빠르게 처리합니다.
input = sys.stdin.readline
# sys.stdout.write를 output 함수로 정의하여 출력을 빠르게 처리합니다.
output = sys.stdout.write

def solve():
    """
    N명의 학생과 M개의 카드를 이용한 번호표 교환 시뮬레이션을 수행합니다.
    """
    try:
        # 1. N (학생 수), M (카드 수) 입력
        N, M = map(int, input().split())

        # 2. N명의 학생이 가진 번호표(A) 입력
        # A = [int(input().strip()) for _ in range(N)]
        # 입력이 N줄에 걸쳐서가 아니라 두 번째 줄부터 N개...
        # "두 번째 줄부터 N줄에 걸쳐서" -> 즉 N개의 라인으로 Ai가 주어집니다.
        A = []
        for _ in range(N):
            A.append(int(input().strip()))

    except Exception:
        # 입력 오류 시 종료
        return

    # 3. 게임 시뮬레이션 시작
    # i는 1번 카드부터 M번 카드까지 순회
    for i in range(1, M + 1):

        # j는 0번 학생(1번째)부터 N-2번 학생(N-1번째)까지 순회
        # (j번 학생과 j+1번 학생을 비교해야 하므로)
        for j in range(N - 1):

            # 4. 비교 및 교환 로직
            # j번 학생의 (번호표 % 카드번호) 값
            val_j = A[j] % i
            # (j+1)번 학생의 (번호표 % 카드번호) 값
            val_j_plus_1 = A[j+1] % i

            # j번 학생의 값이 (j+1)번 학생의 값보다 크면 교환
            if val_j > val_j_plus_1:
                A[j], A[j+1] = A[j+1], A[j]

        # (마지막 N-1번 학생은 카드를 받고 버림 - 로직상 추가 구현 불필요)

    # 5. 최종 결과 출력
    # 각 학생의 번호표를 한 줄에 하나씩 출력
    output_lines = [str(num) for num in A]
    output('\n'.join(output_lines) + '\n')


if __name__ == "__main__":
    solve()