# Gemini 2.5 Pro
import sys

def solve():
    """
    주어진 두 글자(대소문자 포함)를 문장에서 밑줄(_)로 교체하는 문제를 해결합니다.
    """
    case_num = 1
    # 입력의 끝을 나타내는 '# #'이 나올 때까지 무한 반복합니다.
    while True:
        try:
            line = sys.stdin.readline().strip()

            # 종료 조건 확인
            if line == "# #":
                break
            
            # 첫 번째 케이스가 아닐 경우, 케이스 사이에 빈 줄을 출력합니다.
            if case_num > 1:
                print()

            # 교체할 두 소문자를 읽습니다.
            letter1, letter2 = line.split()
            # 대문자 버전도 준비합니다.
            letter1_upper = letter1.upper()
            letter2_upper = letter2.upper()

            # 케이스 번호를 출력합니다.
            print(f"Case {case_num}")

            # 처리할 문장 라인의 수를 읽습니다.
            num_lines = int(sys.stdin.readline())

            # n개의 문장 라인을 순회하며 처리합니다.
            for _ in range(num_lines):
                # 한 줄을 읽습니다. rstrip()을 사용하여 문장 끝의 줄바꿈 문자만 제거합니다.
                text_line = sys.stdin.readline().rstrip('\n')

                # 4개의 글자(소문자 2개, 대문자 2개)에 대해 교체를 수행합니다.
                processed_line = text_line.replace(letter1, '_')
                processed_line = processed_line.replace(letter1_upper, '_')
                processed_line = processed_line.replace(letter2, '_')
                processed_line = processed_line.replace(letter2_upper, '_')

                # 처리된 문장을 출력합니다.
                print(processed_line)
            
            # 다음 케이스를 위해 케이스 번호를 1 증가시킵니다.
            case_num += 1

        except (ValueError, IndexError):
            # 입력이 잘못되거나 비어있는 경우 반복을 중단합니다.
            break

# 메인 함수 실행
solve()