# Gemini 3 Pro
import sys

# 입력을 빠르게 처리하기 위해 sys.stdin.readline 사용
input = sys.stdin.readline

def solve():
    """
    주어진 불리언 연산 (AND 또는 OR)을 수행하고 결과를 출력하는 함수
    """
    try:
        # 단일 입력 라인을 읽고 공백을 기준으로 세 부분으로 나눕니다.
        # 예: "true AND false" -> ["true", "AND", "false"]
        parts = input().strip().split()
        
        if not parts or len(parts) != 3:
            # 입력 형식이 잘못된 경우 처리
            return

        value1_str, operation, value2_str = parts

        # 1. 문자열 'true'/'false'를 파이썬의 불리언 값 True/False로 변환
        # value1: True 또는 False
        value1 = (value1_str == 'true')
        # value2: True 또는 False
        value2 = (value2_str == 'true')
        
        # 2. 연산자에 따라 논리 연산 수행
        result_bool = False
        if operation == 'AND':
            result_bool = value1 and value2
        elif operation == 'OR':
            result_bool = value1 or value2
        else:
            # 정의되지 않은 연산자가 들어올 경우 (문제 조건상 발생하지 않음)
            return

        # 3. 결과를 문자열 "true" 또는 "false"로 출력
        # 파이썬의 불리언 값을 소문자 문자열로 변환합니다.
        print(str(result_bool).lower())

    except Exception:
        # 기타 예외 처리
        pass

if __name__ == "__main__":
    solve()