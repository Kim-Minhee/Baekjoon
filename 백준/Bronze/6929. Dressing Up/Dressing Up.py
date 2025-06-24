# Gemini 2.5 Pro
import sys

def solve_bowtie():
    """
    주어진 높이(H)에 따라 나비넥타이 패턴을 출력하는 함수.
    """
    try:
        # 한 줄을 읽어와서 정수로 변환합니다.
        H = int(sys.stdin.readline())
    except (ValueError, IndexError):
        # 입력이 비어있거나 잘못된 경우 함수를 종료합니다.
        return

    # 나비넥타이의 전체 너비는 2*H 입니다.
    total_width = 2 * H

    # 위쪽 절반을 출력합니다.
    # 가운데 줄 바로 전까지 반복합니다. (0부터 H//2 - 1 까지)
    for i in range(H // 2):
        # 현재 줄의 한쪽에 들어갈 별의 개수를 계산합니다. (1, 3, 5, ...)
        num_stars = 2 * i + 1
        stars_part = '*' * num_stars

        # 가운데 들어갈 공백의 개수를 계산합니다.
        num_spaces = total_width - (2 * num_stars)
        spaces_part = ' ' * num_spaces

        # (왼쪽 별) + (가운데 공백) + (오른쪽 별) 형태로 출력합니다.
        print(stars_part + spaces_part + stars_part)

    # 가운데 한 줄을 출력합니다.
    # 이 줄은 별로 완전히 채워집니다.
    print('*' * total_width)

    # 아래쪽 절반을 출력합니다.
    # 위쪽 절반을 거꾸로 반복하는 것과 같습니다. (H//2 - 1 부터 0 까지)
    for i in range(H // 2 - 1, -1, -1):
        # 별과 공백의 개수를 계산하는 로직은 위쪽 절반과 동일합니다.
        num_stars = 2 * i + 1
        stars_part = '*' * num_stars

        num_spaces = total_width - (2 * num_stars)
        spaces_part = ' ' * num_spaces

        print(stars_part + spaces_part + stars_part)

# 함수 실행
solve_bowtie()