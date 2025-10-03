# Gemini 2.5 Pro
import sys

def solve():
    """
    뺄셈을 이용한 원조 유클리드 호제법으로 두 수의 최대공약수(GCD)를 구합니다.
    """
    try:
        # 한 줄을 읽어 공백을 기준으로 두 개의 숫자로 나눕니다.
        a, b = map(int, sys.stdin.readline().split())

        # 두 수가 같아질 때까지 반복합니다.
        while a != b:
            # a가 b보다 크면, a에서 b를 뺍니다.
            if a > b:
                a = a - b
            # b가 a보다 크면, b에서 a를 뺍니다.
            else:
                b = b - a
        
        # 반복이 끝나면 a와 b는 같아지고, 이 값이 바로 최대공약수입니다.
        print(a)

    except (ValueError, IndexError):
        # 입력이 비어있는 경우를 대비한 예외 처리입니다.
        pass

# 메인 함수 실행
solve()