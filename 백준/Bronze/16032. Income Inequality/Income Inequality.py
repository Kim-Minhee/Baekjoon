# Gemini 3 Pro
import sys

def solve():
    # 빠른 입출력 세팅
    input = sys.stdin.readline
    
    while True:
        # 1. 사람의 수 n 입력
        n = int(input().strip())
        
        # 0이 입력되면 프로그램 종료
        if n == 0:
            break
            
        # 2. n명의 소득 데이터 입력
        incomes = list(map(int, input().split()))
        
        # 전체 소득의 합
        total_income = sum(incomes)
        
        count = 0
        # 3. 평균 이하인 사람 수 세기
        for income in incomes:
            # income <= (total_income / n) 대신
            # 양변에 n을 곱한 정수 수식을 사용하여 소수점 오차 방지
            if income * n <= total_income:
                count += 1
                
        # 결과 출력
        print(count)

if __name__ == '__main__':
    solve()