# Gemini 2.5 Pro
import sys

def solve():
    """
    1부터 20까지의 카드를 주어진 10개의 구간에 따라 역순으로 배치하는 문제를 해결합니다.
    """
    # 1부터 20까지 숫자가 오름차순으로 담긴 리스트를 생성합니다.
    # 이것이 카드의 초기 상태를 나타냅니다.
    cards = list(range(1, 21))

    # 10개의 구간을 입력받기 위해 10번 반복합니다.
    for _ in range(10):
        try:
            # 한 줄을 읽어 공백을 기준으로 나눈 뒤, 각 값을 정수로 변환합니다.
            a, b = map(int, sys.stdin.readline().split())

            # 문제에서는 위치를 1부터 세지만, 파이썬 리스트 인덱스는 0부터 시작합니다.
            # 따라서 시작 위치 a는 인덱스 a-1에 해당합니다.
            # 슬라이싱 cards[start:end]는 start 인덱스부터 end-1 인덱스까지를 의미하므로,
            # 위치 b까지 포함하려면 end 값으로 b를 사용해야 합니다.
            start_index = a - 1
            end_index = b

            # cards 리스트에서 뒤집을 부분을 선택합니다.
            sublist_to_reverse = cards[start_index:end_index]

            # 선택한 부분을 뒤집습니다. [::-1]은 리스트를 역순으로 만드는 슬라이싱 문법입니다.
            reversed_sublist = sublist_to_reverse[::-1]

            # 원본 리스트의 해당 부분을 뒤집힌 부분으로 교체합니다.
            cards[start_index:end_index] = reversed_sublist

        except (ValueError, IndexError):
            # 입력이 잘못된 경우를 대비한 예외 처리입니다.
            continue
    
    # 최종적으로 배치된 카드의 순서를 출력합니다.
    # *cards는 리스트의 각 요소를 공백으로 구분하여 출력해줍니다.
    print(*cards)

# 메인 함수 실행
solve()