# Gemini 2.5 Pro
import sys

def jumble_word(word):
    """
    한 단어의 첫 글자와 마지막 글자를 제외하고 가운데 부분을 뒤집습니다.
    """
    # 단어의 길이가 2 이하이면 변환 없이 그대로 반환합니다.
    if len(word) <= 2:
        return word
    
    # 첫 글자, 마지막 글자, 그리고 가운데 부분을 분리합니다.
    first_char = word[0]
    last_char = word[-1]
    middle_part = word[1:-1]
    
    # 가운데 부분을 뒤집습니다.
    jumbled_middle = middle_part[::-1]
    
    # 분리했던 부분들을 다시 합쳐서 새로운 단어를 만듭니다.
    return first_char + jumbled_middle + last_char

def solve_jumbling():
    """
    입력된 텍스트 줄을 읽어 단어들을 변환하는 메인 함수
    """
    while True:
        # 한 줄을 읽어와서 양쪽 끝의 공백이나 개행 문자를 제거합니다.
        line = sys.stdin.readline().strip()

        # 종료 조건: '#'이 입력되면 루프를 빠져나갑니다.
        if line == '#':
            break

        # 줄을 공백 기준으로 단어 리스트로 나눕니다.
        words = line.split(' ')

        # 각 단어에 대해 jumble_word 함수를 적용하여 새로운 리스트를 만듭니다.
        jumbled_words = [jumble_word(word) for word in words]

        # 변환된 단어 리스트를 다시 하나의 문장으로 합쳐서 출력합니다.
        print(" ".join(jumbled_words))

# 함수 실행
solve_jumbling()