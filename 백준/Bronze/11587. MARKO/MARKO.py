# Gemini 2.5 Pro
import sys

def solve():
    """
    T9 키패드 입력(숫자열)과 일치하는 사전 단어의 개수를 셉니다.
    """

    # 1. 'a'~'z'를 T9 숫자 키에 매핑하는 딕셔너리를 생성합니다.
    t9_map = {}
    key_map_list = [
        ('abc', '2'),
        ('def', '3'),
        ('ghi', '4'),
        ('jkl', '5'),
        ('mno', '6'),
        ('pqrs', '7'),
        ('tuv', '8'),
        ('wxyz', '9')
    ]

    for letters, digit in key_map_list:
        for letter in letters:
            t9_map[letter] = digit

    try:
        # 2. 입력을 받습니다.
        n = int(sys.stdin.readline())

        dictionary = []
        for _ in range(n):
            dictionary.append(sys.stdin.readline().strip())

        # S: 사용자가 누른 키패드 순서
        s = sys.stdin.readline().strip()

    except (ValueError, IndexError, EOFError):
        # 입력이 잘못된 경우
        print(0)
        return

    # 3. 일치하는 단어의 개수를 셉니다.
    match_count = 0
    s_len = len(s) # 비교를 위해 길이를 미리 저장

    # 사전의 모든 단어를 순회합니다.
    for word in dictionary:

        # (필터 1) 길이 확인
        if len(word) != s_len:
            continue

        # (필터 2) 글자별 매칭 확인
        is_match = True
        for i in range(s_len):
            letter = word[i]
            digit = s[i]

            # 매핑 테이블에서 해당 글자가 어떤 숫자에 속하는지 확인
            expected_digit = t9_map[letter]

            # 사용자가 누른 숫자와 일치하지 않으면, 이 단어는 탈락입니다.
            if expected_digit != digit:
                is_match = False
                break # 다음 단어로 넘어갑니다.

        # 모든 글자가 일치했다면, 카운트를 증가시킵니다.
        if is_match:
            match_count += 1

    # 4. 최종 결과를 출력합니다.
    print(match_count)

# 메인 함수 실행
if __name__ == "__main__":
    solve()