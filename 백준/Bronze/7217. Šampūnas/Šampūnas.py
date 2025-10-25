# Gemini 2.5 Pro -> 
# -*- coding: utf-8 -*-
import sys

def solve_bitlandia_wash_count():
    """
    N일 동안 비트란디야 주민들이 머리를 감는 총 횟수를 계산합니다.
    
    문제 조건:
    1. 첫날(1일)에는 무조건 머리를 감습니다.
    2. 공휴일에는 무조건 머리를 감습니다.
    3. 공휴일이 아니더라도, 전날 머리를 감지 않았다면 오늘 감습니다.
    """
    
    # 입력 처리: N (총 기간), K (공휴일 수)
    try:
        # 첫 번째 줄에서 N과 K를 읽어옵니다. (띄어쓰기로 구분)
        line1 = sys.stdin.readline().strip()
        if not line1:
            # 입력이 없으면 조용히 종료합니다.
            return
            
        n, k = map(int, line1.split())
        
        # 공휴일 목록을 읽어옵니다.
        holidays = set()
        for _ in range(k):
            holiday_line = sys.stdin.readline().strip()
            if holiday_line:
                holidays.add(int(holiday_line))
            
    except (ValueError, IndexError):
        # 입력이 예상과 다를 경우 (예: 숫자가 아닌 문자 등) 오류 처리 후 종료합니다.
        # 실제 환경에서 이 오류는 사용자에게 보여지는 런타임 오류가 될 수 있습니다.
        return

    # ----------------------------------------------------
    # 핵심 로직
    # ----------------------------------------------------
    
    # 초기 상태 설정: 첫날(1일)은 항상 머리를 감습니다.
    wash_count = 1
    washed_yesterday = True 
    
    # 2일부터 N일까지 시뮬레이션을 시작합니다.
    for day in range(2, n + 1):
        wash_today = False # 오늘 머리를 감을지 여부 초기화
        
        # 규칙 1: 오늘이 공휴일인 경우
        if day in holidays:
            wash_today = True
        # 규칙 2: 공휴일이 아니더라도, 어제 머리를 감지 않은 경우
        elif not washed_yesterday:
            wash_today = True
            
        # 횟수 업데이트
        if wash_today:
            wash_count += 1
            
        # 다음 날을 위해 '어제 감았는지' 상태를 업데이트합니다.
        washed_yesterday = wash_today

    # 최종 결과를 출력합니다.
    print(wash_count)

if __name__ == "__main__":
    # 스크립트가 직접 실행될 때 함수를 호출합니다.
    solve_bitlandia_wash_count()