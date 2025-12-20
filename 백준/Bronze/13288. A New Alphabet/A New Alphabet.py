# Gemini 3 Pro
import sys

# 입력을 빠르게 처리하기 위해 sys.stdin.readline 사용
input = sys.stdin.readline

def solve():
    """
    New Alphabet 번역기
    ASCII 텍스트를 문제에서 정의된 새로운 심볼 세트로 변환합니다.
    """
    # 1. 변환 테이블 정의 (소문자 기준)
    # 딕셔너리를 사용하여 O(1) 시간에 매핑된 문자열을 찾을 수 있습니다.
    mapping = {
        'a': '@', 
        'b': '8', 
        'c': '(', 
        'd': '|)', 
        'e': '3', 
        'f': '#', 
        'g': '6', 
        'h': '[-]', 
        'i': '|', 
        'j': '_|', 
        'k': '|<', 
        'l': '1', 
        'm': '[]\/[]', 
        'n': '[]\[]', 
        'o': '0', 
        'p': '|D', 
        'q': '(,)', 
        'r': '|Z', 
        's': '$', 
        't': "']['", 
        'u': '|_|', 
        'v': '\/', 
        'w': '\/\/', 
        'x': '}{', 
        'y': '`/', 
        'z': '2'
    }

    try:
        # 2. 텍스트 입력
        # rstrip('\n')을 사용하여 줄바꿈 문자만 제거합니다. 
        # (문장 끝의 공백은 유지해야 할 수 있으므로 strip() 대신 사용)
        text = input().rstrip('\n')
        
        if not text:
            # 입력이 없을 경우 빈 줄 출력 (문제 조건상 드물겠지만 안전장치)
            # 하지만 문제에서 "Input contains one line"이라 했으므로 넘어갈 수 있음.
            # 다만 백준 등에서는 빈 입력도 고려하는 것이 좋습니다.
             pass

        # 3. 변환 로직
        result = []
        for char in text:
            # 대소문자 구분 없이 변환하므로 소문자로 변경하여 키를 찾습니다.
            lower_char = char.lower()
            
            # 딕셔너리에 있으면 변환된 문자열을, 없으면 원래 문자를 그대로 추가합니다.
            if lower_char in mapping:
                result.append(mapping[lower_char])
            else:
                result.append(char)
        
        # 4. 리스트를 문자열로 합쳐서 출력
        print("".join(result))

    except Exception:
        pass

if __name__ == "__main__":
    solve()