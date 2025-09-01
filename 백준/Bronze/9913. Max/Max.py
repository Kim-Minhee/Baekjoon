# Gemini 2.5 Pro
import sys

# 빠른 입력을 위해 sys.stdin.readline 사용
# 참고: Jupyter Notebook과 같은 일부 환경에서는 sys.stdin.readline이 제대로 동작하지 않을 수 있습니다.
# 그럴 경우 input() 함수를 직접 사용하시면 됩니다.
input = sys.stdin.readline

def solve():
    """가장 높은 빈도수를 찾는 문제를 해결하는 메인 함수"""
    try:
        # 시퀀스에 포함된 정수의 개수 N을 입력받습니다.
        n = int(input())
        
        # 숫자의 빈도를 저장할 리스트를 생성합니다.
        # 숫자의 범위가 1~1000이므로, 인덱스를 편리하게 사용하기 위해 1001칸으로 만듭니다.
        # frequency[i]는 숫자 i가 등장한 횟수를 의미합니다.
        frequency = [0] * 1001
        
        # N개의 정수를 입력받아 빈도를 계산합니다.
        for _ in range(n):
            num = int(input())
            # 입력받은 숫자에 해당하는 인덱스의 값을 1 증가시킵니다.
            frequency[num] += 1
            
        # frequency 리스트에서 가장 큰 값이 바로 가장 높은 빈도수입니다.
        highest_freq = max(frequency)
        
        # 결과를 출력합니다.
        print(highest_freq)

    except (ValueError, IndexError):
        # 입력이 비어있거나 형식이 잘못된 경우를 대비한 예외 처리
        pass

# 메인 함수 실행
solve()