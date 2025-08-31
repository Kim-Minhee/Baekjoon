# Gemini 2.5 Pro
import sys

# 빠른 입력을 위해 sys.stdin.readline 사용
input = sys.stdin.readline

def solve():
    """직원 생일 통계 문제를 해결하는 메인 함수"""
    
    # 12개의 달에 대한 생일자 수를 저장할 리스트를 생성합니다.
    # 인덱스를 1부터 12까지 편리하게 사용하기 위해 13칸으로 만듭니다. (0번 인덱스는 사용 안 함)
    month_counts = [0] * 13
    
    try:
        # 직원의 수를 입력받습니다.
        num_employees = int(input())
        
        # 직원 수만큼 반복합니다.
        for _ in range(num_employees):
            # 한 줄을 입력받아 공백으로 분리합니다. (예: ['1234', '15/08/1990'])
            line_parts = input().split()
            # 날짜 문자열을 가져옵니다. (예: '15/08/1990')
            date_string = line_parts[1]
            # '/'를 기준으로 날짜를 분리하고, 월(month) 부분만 가져옵니다.
            month = int(date_string.split('/')[1])
            
            # 해당하는 월의 카운트를 1 증가시킵니다.
            month_counts[month] += 1
            
        # 모든 입력 처리가 끝난 후, 1월부터 12월까지 결과를 출력합니다.
        for i in range(1, 13):
            # 형식: (월) (인원수)
            print(f"{i} {month_counts[i]}")

    except (ValueError, IndexError):
        # 입력 관련 예외 처리
        pass

# 메인 함수 실행
solve()