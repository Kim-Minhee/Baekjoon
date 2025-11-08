# Gemini 2.5 Pro
import sys

def solve():
    """
    아핀 암호 E(X) = (aX + b) mod 26을 적용하여
    주어진 평문을 암호문으로 변환합니다.
    """
    try:
        # 첫 줄에서 테스트 케이스의 개수 T를 읽습니다.
        num_test_cases = int(sys.stdin.readline())
    except (ValueError, IndexError):
        return

    # 각 테스트 케이스를 순회합니다.
    for _ in range(num_test_cases):
        try:
            # a와 b 값을 읽습니다.
            a, b = map(int, sys.stdin.readline().split())

            # 평문 문자열을 읽고, 끝의 줄바꿈 문자를 제거합니다.
            plaintext = sys.stdin.readline().strip()

            # 변환된 문자들을 저장할 리스트를 생성합니다.
            # (문자열에 바로 더하는 것보다 리스트에 모았다가 합치는 것이 훨씬 빠릅니다)
            encrypted_chars = []

            # 평문의 각 문자를 순회합니다.
            for char in plaintext:
                # 1. 문자를 숫자(0~25)로 변환합니다.
                #    (ord('A')는 65입니다. 'A' -> 65-65=0, 'B' -> 66-65=1)
                x = ord(char) - ord('A')

                # 2. 아핀 암호 공식을 적용합니다.
                encrypted_value = (a * x + b) % 26

                # 3. 결과 숫자(0~25)를 다시 문자(A~Z)로 변환합니다.
                #    (0 -> 65+0=65 -> 'A', 1 -> 65+1=66 -> 'B')
                encrypted_char = chr(ord('A') + encrypted_value)

                # 결과를 리스트에 추가합니다.
                encrypted_chars.append(encrypted_char)

            # 변환된 모든 문자를 하나의 문자열로 합쳐 출력합니다.
            print("".join(encrypted_chars))

        except (ValueError, IndexError, EOFError):
            # 입력이 잘못되거나 파일이 끝난 경우 다음 테스트 케이스로 넘어갑니다.
            continue

# 메인 함수 실행
if __name__ == "__main__":
    solve()