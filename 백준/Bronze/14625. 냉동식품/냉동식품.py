# Gemini 3 Pro
import sys

# 입력을 빠르게 처리하기 위해 sys.stdin.readline 사용
input = sys.stdin.readline

def solve():
    """
    백준 14625번: 냉동식품
    시작 시간부터 종료 시간까지 1분씩 증가하며,
    HH:MM 형식에 숫자 N이 포함된 횟수를 셉니다.
    """
    try:
        # 시작 시간 H, M 입력
        start_h, start_m = map(int, input().split())
        # 종료 시간 H, M 입력
        end_h, end_m = map(int, input().split())
        # 찾을 숫자 N 입력
        n = int(input().strip())
        
        # 모든 시간을 00:00 기준 '분' 단위로 변환
        current_time = start_h * 60 + start_m
        end_time = end_h * 60 + end_m
        
        count = 0
        
        # 시작 시간부터 종료 시간까지(포함) 1분씩 증가하며 확인
        while current_time <= end_time:
            # 현재 분을 다시 시(H)와 분(M)으로 변환
            # (문제 조건상 날짜가 바뀌지 않으므로 % 24 처리는 필수가 아니지만 안전을 위해 포함 가능)
            hh = (current_time // 60) % 24
            mm = current_time % 60
            
            # HH:MM 형식으로 문자열 생성 (두 자리 숫자로 포맷팅)
            # f"{hh:02d}"는 5 -> "05" 처럼 0을 채워줍니다.
            time_str = f"{hh:02d}{mm:02d}"
            
            # 숫자 N이 문자열에 포함되어 있는지 확인
            if str(n) in time_str:
                count += 1
            
            # 1분 증가
            current_time += 1
            
        print(count)

    except ValueError:
        pass

if __name__ == "__main__":
    solve()