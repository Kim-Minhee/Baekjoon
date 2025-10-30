# Gemini 2.5 Pro
import sys
from collections import Counter

def solve():
    """
    주어진 쿠키 상자의 문자로 각 단어를 만들 수 있는지 확인합니다.
    """
    # 빠른 입력을 위해 설정
    input = sys.stdin.readline

    try:
        # 테스트 케이스 개수 T를 읽습니다.
        T = int(input().strip())
    except:
        return

    # T번의 테스트 케이스를 처리합니다.
    for _ in range(T):
        # 1. 쿠키 상자의 문자 목록을 읽습니다.
        # 모든 문자는 대문자(A-Z)입니다.
        cookie_box_letters = input().strip()

        # 2. 쿠키 상자의 문자 빈도수를 계산합니다. (기준점)
        # 예: "HELLO" -> {'H': 1, 'E': 1, 'L': 2, 'O': 1}
        cookie_counts = Counter(cookie_box_letters)

        # 3. 만들고 싶은 단어의 개수 W를 읽습니다.
        try:
            W = int(input().strip())
        except:
            continue

        # 4. W개의 단어 각각에 대해 확인합니다.
        for _ in range(W):
            word = input().strip()

            # 5. 현재 단어에 필요한 문자 빈도수를 계산합니다.
            word_counts = Counter(word)

            # 단어를 만들 수 있는지 여부를 저장할 플래그
            is_possible = True

            # 6. 단어에 필요한 각 문자(char)에 대해 쿠키 상자의 재고와 비교합니다.
            for char, required_count in word_counts.items():
                # 쿠키 상자에 해당 문자가 몇 개 있는지 확인합니다.
                # get(char, 0)을 사용하여 해당 문자가 쿠키 상자에 없으면 0을 반환합니다.
                available_count = cookie_counts.get(char, 0)

                # 필요한 개수가 가진 개수보다 많으면 만들 수 없습니다.
                if required_count > available_count:
                    is_possible = False
                    break # 더 이상 확인할 필요가 없으므로 루프를 종료합니다.

            # 7. 결과 출력
            if is_possible:
                print("YES")
            else:
                print("NO")

if __name__ == "__main__":
    solve()