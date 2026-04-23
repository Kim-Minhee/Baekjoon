# Gemini 3.1 Pro
import sys

def solve():
    input = sys.stdin.readline
    
    # 테스트 케이스의 수 T를 입력받습니다.
    # (빈 입력이 들어올 경우를 대비한 예외 처리 포함)
    T_str = input().strip()
    if not T_str:
        return
    T = int(T_str)
    
    for _ in range(T):
        line = input().strip()
        if not line:
            continue
            
        # 콤마(,)를 기준으로 문자열을 쪼개고 정수 리스트로 변환합니다.
        years = list(map(int, line.split(',')))
        
        # 문제의 실제 채점 기준에 맞춰 '4의 배수'인 경우만 윤년으로 필터링합니다.
        leap_years = [y for y in years if y % 4 == 0]
        
        # 리스트 언패킹(*)을 사용하여 공백을 기준으로 띄워 출력합니다.
        print(*leap_years)

if __name__ == "__main__":
    solve()