# Gemini 2.5 Pro
import sys

def solve():
    """참가자 비밀번호 생성 문제를 해결하는 메인 함수"""
    try:
        # 첫 줄에서 테스트 케이스의 개수를 읽습니다.
        num_test_cases = int(sys.stdin.readline())
    except (ValueError, IndexError):
        # 입력이 비어있거나 잘못된 경우 함수를 종료합니다.
        num_test_cases = 0

    # 각 테스트 케이스를 순회합니다.
    for i in range(1, num_test_cases + 1):
        # 첫 번째 테스트 케이스가 아닐 경우, 문제의 요구사항에 따라 빈 줄을 출력합니다.
        if i > 1:
            print()

        # 시나리오 번호를 출력합니다.
        print(f"Scenario #{i}:")

        try:
            # 단어의 개수(m)를 읽습니다.
            num_words = int(sys.stdin.readline())
            # m개의 단어를 읽어 리스트에 저장합니다.
            # .strip()을 사용하여 각 단어의 앞뒤 공백(줄바꿈 문자 등)을 제거합니다.
            words = [sys.stdin.readline().strip() for _ in range(num_words)]

            # 참가자의 수(n)를 읽습니다.
            num_participants = int(sys.stdin.readline())

            # 각 참가자를 순회합니다.
            for _ in range(num_participants):
                # 비밀번호 정보를 한 줄로 읽고, 공백을 기준으로 나눠 숫자로 변환합니다.
                info = list(map(int, sys.stdin.readline().split()))
                
                # 첫 번째 숫자는 단어의 개수(k)이고, 나머지가 실제 단어 인덱스입니다.
                indices = info[1:]

                # 인덱스에 해당하는 단어들을 리스트에서 찾아 하나의 문자열로 합칩니다.
                # password = ""
                # for index in indices:
                #     password += words[index]
                # 위와 같이 문자열을 반복해서 더하는 것보다, 리스트에 모아 join하는 것이 더 효율적입니다.
                password_parts = [words[index] for index in indices]
                password = "".join(password_parts)

                # 완성된 비밀번호를 출력합니다.
                print(password)

        except (ValueError, IndexError):
            # 테스트 케이스 중간에 입력이 잘못된 경우 다음 케이스로 넘어갑니다.
            continue

# 메인 함수 실행
solve()