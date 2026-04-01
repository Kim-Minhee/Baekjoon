# Gemini 3.1 Pro
import sys

def solve():
    # 개행 문자(\n)만 제거하여 입력받습니다. (공백 등 출력 가능한 다른 문자가 포함될 수 있으므로 strip() 대신 rstrip('\n') 사용)
    T = sys.stdin.readline().rstrip('\n')
    
    if not T:
        return
        
    # 1. 암호 키(key) 알아내기
    # 원래 문자열의 첫 글자는 무조건 'C'이므로, 암호문의 첫 글자 T[0]과 XOR 하면 key가 나옵니다.
    key = ord(T[0]) ^ ord('C')
    
    # 2. 알아낸 key를 이용하여 전체 문자열 복호화하기
    result = []
    for char in T:
        # 문자의 아스키코드에 key를 XOR 연산한 뒤, 다시 문자(chr)로 변환합니다.
        decrypted_char = chr(ord(char) ^ key)
        result.append(decrypted_char)
        
    # 복호화된 문자열을 합쳐서 출력합니다.
    print("".join(result))

if __name__ == '__main__':
    solve()