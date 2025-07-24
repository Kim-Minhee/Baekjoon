# Gemini 2.5 Pro
import sys

def solve_chair_placement():
    """
    A x B 테이블에 K x K 의자를 최대한 많이 놓는 수를 계산합니다.
    """
    try:
        # 한 줄을 읽어와서 A, B, K로 분리합니다.
        A, B, K = map(int, sys.stdin.readline().split())
    except (ValueError, IndexError):
        # 입력이 비었거나 형식이 잘못된 경우 종료합니다.
        return

    # 테이블의 각 변을 "의자 단위"로 변환합니다.
    # a: A 길이에 놓을 수 있는 최대 의자 수
    # b: B 길이에 놓을 수 있는 최대 의자 수
    chairs_along_A = A // K
    chairs_along_B = B // K

    max_chairs = 0

    # 경우 1: 테이블의 폭이나 너비가 의자보다 작은 경우
    # 의자를 하나도 놓을 수 없습니다.
    if chairs_along_A == 0 or chairs_along_B == 0:
        max_chairs = 0
    
    # 경우 2: 테이블의 폭이나 너비가 의자 2개 깊이보다 좁은 경우
    # 이 경우, 의자를 마주보게 양쪽에 놓을 수 없으며, 모서리가 겹치는 문제가 발생합니다.
    # 가장 효율적인 방법은 가장 긴 변을 따라 한 줄로만 의자를 놓는 것입니다.
    elif chairs_along_A == 1 or chairs_along_B == 1:
        # 예를 들어, chairs_along_B가 1이면, 테이블 폭이 좁아 A-길이의 양쪽에 놓을 수 없습니다.
        # 따라서 A-길이를 따라 한 줄만 놓는 것이 최선입니다.
        # chairs_along_A * chairs_along_B는 이 상황을 간결하게 표현합니다.
        # (예: b=1이면 a*b = a, a=1이면 a*b = b)
        max_chairs = chairs_along_A * chairs_along_B

    # 경우 3: 테이블이 충분히 넓어 네 변을 모두 활용할 수 있는 경우
    # 네 변의 의자 수를 모두 더한 뒤, 모서리에서 겹치는 4개를 뺍니다.
    else:
        max_chairs = 2 * (chairs_along_A + chairs_along_B - 2)

    print(max_chairs)

# 함수 실행
solve_chair_placement()