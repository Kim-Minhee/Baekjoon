# Gemini 3 Pro
import sys

# 대량의 입력을 빠르게 처리하기 위해 sys.stdin.readline 사용
input = sys.stdin.readline

def solve():
    """
    구글 I/O 문자열 디코더
    'I'는 1로, 'O'는 0으로 변환하여 아스키 문자로 복원합니다.
    """
    try:
        # 첫 줄: 테스트 케이스의 개수 T
        line = input().strip()
        if not line:
            return
        T = int(line)

        for i in range(1, T + 1):
            # 둘째 줄: 문자열의 바이트 수 B (글자 수)
            line = input().strip()
            if not line:
                break
            B = int(line)
            
            # 셋째 줄: 8 * B 길이의 인코딩된 문자열
            encoded_str = input().strip()
            
            decoded_chars = []
            
            # 문자열을 8글자(1바이트)씩 끊어서 처리합니다.
            # range(시작, 끝, 스텝)을 사용하여 0, 8, 16... 인덱스로 접근
            for j in range(0, len(encoded_str), 8):
                # 8글자 슬라이싱
                byte_chunk = encoded_str[j:j+8]
                
                # 변환 로직:
                # 1. 'I' -> '1', 'O' -> '0' 으로 문자열 치환
                # 2. int(string, 2)를 사용하여 2진수 문자열을 10진수 정수로 변환
                # 3. chr() 함수를 사용하여 정수를 아스키 문자로 변환
                char = chr(int(byte_chunk.replace('I', '1').replace('O', '0'), 2))
                
                decoded_chars.append(char)
            
            # 리스트에 모아둔 문자들을 하나의 문자열로 결합
            result_message = "".join(decoded_chars)
            
            # 결과 출력 (f-string 사용)
            print(f"Case #{i}: {result_message}")
            
    except ValueError:
        pass

if __name__ == "__main__":
    solve()