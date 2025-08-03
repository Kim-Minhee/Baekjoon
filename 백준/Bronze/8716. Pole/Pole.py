# Gemini 2.5 Pro
import sys

def solve_intersection_area():
    """
    두 직사각형의 겹치는 부분의 넓이를 계산합니다.
    """
    try:
        # 첫 번째 직사각형의 좌표를 읽어옵니다.
        x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
        # 두 번째 직사각형의 좌표를 읽어옵니다.
        x3, y3, x4, y4 = map(int, sys.stdin.readline().split())
    except (ValueError, IndexError):
        # 입력이 비었거나 형식이 잘못된 경우 0을 출력하고 종료합니다.
        print(0)
        return

    # 겹치는 영역의 x좌표를 계산합니다.
    # 왼쪽 경계는 두 왼쪽 경계 중 큰 값, 오른쪽 경계는 두 오른쪽 경계 중 작은 값입니다.
    inter_x1 = max(x1, x3)
    inter_x2 = min(x2, x4)

    # 겹치는 영역의 y좌표를 계산합니다.
    # 위쪽 경계는 두 위쪽 경계 중 작은 값, 아래쪽 경계는 두 아래쪽 경계 중 큰 값입니다.
    inter_y1 = min(y1, y3)
    inter_y2 = max(y2, y4)

    # 겹치는 영역의 가로와 세로 길이를 계산합니다.
    width = inter_x2 - inter_x1
    height = inter_y1 - inter_y2

    # 가로나 세로 길이가 0 이하이면 겹치지 않는 것이므로 넓이는 0입니다.
    if width <= 0 or height <= 0:
        area = 0
    else:
        area = width * height

    # 최종 넓이를 출력합니다.
    print(area)

# 함수 실행
solve_intersection_area()