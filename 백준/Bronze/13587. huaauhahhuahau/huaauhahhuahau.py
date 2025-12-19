# Gemini 3 Pro
import sys

# 입력을 빠르게 처리하기 위해 sys.stdin.readline 사용
input = sys.stdin.readline

def solve():
    """
    디지털 웃음 판별 함수
    문자열에서 모음만 추출하여 팰린드롬(앞뒤가 똑같은지) 여부를 확인합니다.
    """
    try:
        # 문자열 입력 및 양쪽 공백 제거
        laugh = input().strip()
        
        if not laugh:
            return

        # 모음 정의
        vowels = set('aeiou')
        
        # 문자열에서 모음만 순서대로 추출하여 리스트 생성
        # 예: "huaauhahhuahau" -> ['u', 'a', 'a', 'u', 'a', 'u', 'a', 'a', 'u']
        extracted_vowels = [char for char in laugh if char in vowels]
        
        # 추출된 모음 리스트가 뒤집었을 때와 같은지 확인 (팰린드롬)
        # 리스트 슬라이싱 [::-1]은 리스트를 역순으로 뒤집습니다.
        if extracted_vowels == extracted_vowels[::-1]:
            print("S")
        else:
            print("N")

    except ValueError:
        pass

if __name__ == "__main__":
    solve()