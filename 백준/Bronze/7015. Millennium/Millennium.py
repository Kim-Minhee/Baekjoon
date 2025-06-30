# Gemini 2.5 Pro
import sys

def get_total_days_before(year, month, day):
    """
    1년 1월 1일부터 주어진 날짜(Y, M, D)가 시작되기 전까지의 총 일수를 계산합니다.
    """
    total_days = 0

    # 1. 지난 해들의 총 일수 계산 (1년부터 year-1년까지)
    for y in range(1, year):
        # 3의 배수인 해는 특별한 해 (200일)
        if y % 3 == 0:
            total_days += 200
        # 그 외에는 일반적인 해 (195일)
        else:
            total_days += 195

    # 2. 현재 해의 지난 달들의 총 일수 계산 (1월부터 month-1월까지)
    is_current_year_special = (year % 3 == 0)
    for m in range(1, month):
        if is_current_year_special:
            total_days += 20  # 특별한 해는 모든 달이 20일
        else:
            # 일반적인 해는 홀수 달이 20일, 짝수 달이 19일
            if m % 2 == 1:  # 홀수 달 (큰 달)
                total_days += 20
            else:  # 짝수 달 (작은 달)
                total_days += 19

    # 3. 현재 달의 지난 일수 계산 (1일부터 day-1일까지)
    total_days += (day - 1)
    
    return total_days

def solve():
    """
    메인 로직을 처리하는 함수
    """
    # 목표일(1000년 1월 1일)까지의 총 일수를 미리 계산해 둡니다.
    days_until_millennium = get_total_days_before(1000, 1, 1)

    try:
        # 첫 줄에서 테스트 케이스의 수를 읽어옵니다.
        num_datasets = int(sys.stdin.readline())
    except (ValueError, IndexError):
        return

    # 각 데이터셋에 대해 반복합니다.
    for _ in range(num_datasets):
        try:
            # 생년월일을 입력받습니다.
            birth_year, birth_month, birth_day = map(int, sys.stdin.readline().split())
        except (ValueError, IndexError):
            continue

        # 생년월일까지의 총 일수를 계산합니다.
        days_until_birth = get_total_days_before(birth_year, birth_month, birth_day)

        # 두 날짜의 차이를 계산하여 출력합니다.
        days_lived = days_until_millennium - days_until_birth
        print(days_lived)

# 함수 실행
solve()