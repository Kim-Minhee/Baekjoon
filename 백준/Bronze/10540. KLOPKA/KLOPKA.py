# Gemini 2.5 Pro
import sys

def solve():
    """
    N개의 모기 위치를 모두 덮을 수 있는 가장 작은 정사각형 상자의 넓이를 계산합니다.
    """
    try:
        # 첫 줄에서 모기의 수 N을 읽습니다.
        num_mosquitoes = int(sys.stdin.readline())

        # X 좌표와 Y 좌표의 최소/최대값을 저장할 변수를 초기화합니다.
        # 문제의 좌표 범위(1 <= X, Y <= 100)를 고려하여 적절한 초기값을 설정합니다.
        min_x = 101 # X의 최대값보다 크게 초기화
        max_x = 0   # X의 최소값보다 작게 초기화
        min_y = 101 # Y의 최대값보다 크게 초기화
        max_y = 0   # Y의 최소값보다 작게 초기화

        # N개의 모기 위치를 순회하며 최소/최대 X, Y 좌표를 갱신합니다.
        for _ in range(num_mosquitoes):
            x, y = map(int, sys.stdin.readline().split())

            if x < min_x:
                min_x = x
            if x > max_x:
                max_x = x

            if y < min_y:
                min_y = y
            if y > max_y:
                max_y = y

        # 최소 필요한 너비와 높이를 계산합니다.
        required_width = max_x - min_x
        required_height = max_y - min_y

        # 정사각형의 한 변의 길이는 너비와 높이 중 더 큰 값이어야 합니다.
        side_length = max(required_width, required_height)

        # 상자의 넓이는 한 변의 길이의 제곱입니다.
        area = side_length ** 2

        # 계산된 넓이를 출력합니다.
        print(area)

    except (ValueError, IndexError):
        # 입력이 잘못된 경우를 대비한 예외 처리입니다.
        pass

# 메인 함수 실행
solve()