# Gemini 2.5 Pro
import sys

def solve_caesar_cipher():
    """
    주어진 단서(원본 첫 글자)를 이용해 카이사르 암호를 해독합니다.
    """
    try:
        # 첫 줄에서 테스트 케이스의 수를 읽어옵니다.
        num_test_cases = int(sys.stdin.readline())
    except (ValueError, IndexError):
        return

    # 각 테스트 케이스에 대해 반복합니다.
    for _ in range(num_test_cases):
        try:
            # 메시지 길이 N을 읽습니다. (실제 계산에는 사용되지 않습니다)
            N = int(sys.stdin.readline())
            # 암호화된 메시지를 읽어옵니다.
            encrypted_message = sys.stdin.readline().strip()
            # 원본 메시지의 첫 글자를 읽어옵니다.
            original_first_char = sys.stdin.readline().strip()
        except (ValueError, IndexError):
            continue

        # 1. 이동 값(K)을 계산합니다.
        # ord(문자)는 문자의 아스키 코드 값을 반환합니다. ord('a')를 빼면 0-기반 인덱스가 됩니다.
        encrypted_first_idx = ord(encrypted_message[0]) - ord('a')
        original_first_idx = ord(original_first_char) - ord('a')
        
        # K = (암호화된 인덱스 - 원본 인덱스) % 26
        K = (encrypted_first_idx - original_first_idx) % 26

        # 2. 전체 메시지를 복호화합니다.
        decrypted_chars = []
        for char in encrypted_message:
            encrypted_idx = ord(char) - ord('a')
            
            # 복호화 공식을 적용합니다.
            decrypted_idx = (encrypted_idx - K) % 26
            
            # 계산된 인덱스를 다시 문자로 변환하여 리스트에 추가합니다.
            decrypted_chars.append(chr(decrypted_idx + ord('a')))
            
        # 복호화된 문자들을 하나의 문자열로 합쳐서 출력합니다.
        print("".join(decrypted_chars))

# 함수 실행
solve_caesar_cipher()