# Gemini 2.5 Pro
import sys

def solve_letter_counter():
    """
    입력된 텍스트에서 각 알파벳 글자의 출현 횟수를 셉니다.
    """
    try:
        # 첫 줄에서 분석할 라인의 수를 읽어옵니다.
        num_lines = int(sys.stdin.readline())
    except (ValueError, IndexError):
        return

    # 각 문자의 개수를 저장할 딕셔너리를 생성합니다.
    char_counts = {}

    # N개의 라인을 읽어와서 글자 수를 셉니다.
    for _ in range(num_lines):
        # .strip()은 불필요한 양끝 공백을 제거할 수 있습니다.
        line = sys.stdin.readline().strip() 
        for char in line:
            # 공백이 아닌 알파벳인 경우에만 카운트합니다.
            if char != ' ':
                # .get(key, 0)은 딕셔너리에 키가 없으면 기본값 0을 반환하여
                # 코드를 간결하게 만들어 줍니다.
                char_counts[char] = char_counts.get(char, 0) + 1

    # --- 결과 출력 ---
    
    # 기준이 될 알파벳 문자열을 정의합니다.
    lowercase_alphabet = "abcdefghijklmnopqrstuvwxyz"
    uppercase_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # 소문자 'a'부터 'z'까지 순서대로 출력합니다.
    for char in lowercase_alphabet:
        # 딕셔너리에 해당 문자가 키로 존재하는 경우에만 출력합니다.
        if char in char_counts:
            print(f"{char} {char_counts[char]}")

    # 대문자 'A'부터 'Z'까지 순서대로 출력합니다.
    for char in uppercase_alphabet:
        if char in char_counts:
            print(f"{char} {char_counts[char]}")

# 함수 실행
solve_letter_counter()