# Gemini 3 Pro
import sys
import math

def solve():
    # 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    K = int(input_data[0])
    P = int(input_data[1])
    X = int(input_data[2])

    # 비용 계산 함수
    def calculate_cost(m):
        # m은 페인트공의 수 (0이면 안됨)
        if m < 1:
            return float('inf')
        return (X * m) + (K * P / m)

    # 1. 수학적으로 이상적인 M 계산 (실수 형태)
    # Total Cost = M*X + (K*P)/M
    # 미분하면 최적의 M = sqrt((K*P)/X)
    optimal_m_float = math.sqrt((K * P) / X)

    # 2. 정수여야 하므로, 해당 값의 앞, 뒤 정수를 후보로 선정
    m_floor = int(optimal_m_float)
    m_ceil = m_floor + 1

    # 3. 두 후보에 대해 비용을 계산하고 최소값 선택
    cost1 = calculate_cost(m_floor)
    cost2 = calculate_cost(m_ceil)

    min_cost = min(cost1, cost2)

    # 4. 소수점 셋째 자리까지 출력
    print(f"{min_cost:.3f}")

if __name__ == "__main__":
    solve()