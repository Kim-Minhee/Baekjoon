# Gemini 2.5 Pro
import sys

def calculate_happiness(capacity, initial_h, decrease_d):
    """
    등차수열의 합 공식을 이용해 특정 동물의 총 행복도를 계산합니다.
    
    Args:
        capacity: 해당 농장에서 키울 수 있는 동물의 최대 수
        initial_h: 첫 동물이 주는 행복도
        decrease_d: 한 마리 늘어날 때마다 감소하는 행복도
        
    Returns:
        해당 농장에서 얻을 수 있는 총 행복도
    """
    # 감소량이 0이면 모든 동물이 동일한 행복도를 제공합니다.
    if decrease_d == 0:
        return capacity * initial_h
    
    # 행복도가 0 이상인 유닛의 개수를 계산합니다.
    # 예: M=10, D=3 -> 10, 7, 4, 1 (4개). 10 // 3 + 1 = 4
    num_positive_terms = initial_h // decrease_d + 1
    
    # 실제로 행복도를 생산하는 동물의 수는 농장의 수용량과 
    # 행복도가 0 이상인 유닛의 수 중 더 작은 값입니다.
    num_producing_animals = min(capacity, num_positive_terms)
    
    n = num_producing_animals
    
    # 등차수열의 합 공식: n/2 * (2*첫째항 + (n-1)*공차)
    # 여기서는 감소하므로 공차가 음수입니다.
    # n/2 * (2*M - (n-1)*D)
    total = n * (2 * initial_h - (n - 1) * decrease_d) // 2
    return total

def solve():
    """
    각 농장에서 소와 벌 중 더 높은 행복도를 주는 쪽을 선택하여
    총 행복도의 최댓값을 계산합니다.
    """
    try:
        m, d_m = map(int, sys.stdin.readline().split())
        h, d_h = map(int, sys.stdin.readline().split())
        num_fields = int(sys.stdin.readline())

        total_happiness = 0

        for _ in range(num_fields):
            c, b = map(int, sys.stdin.readline().split())

            # 각 농장에 소를 키웠을 때와 벌을 키웠을 때의 행복도를 각각 계산합니다.
            milk_happiness = calculate_happiness(c, m, d_m)
            honey_happiness = calculate_happiness(b, h, d_h)
            
            # 둘 중 더 큰 값을 총 행복도에 더합니다.
            total_happiness += max(milk_happiness, honey_happiness)
            
        print(total_happiness)

    except (ValueError, IndexError):
        # 입력이 잘못된 경우를 대비한 예외 처리입니다.
        pass

# 메인 함수 실행
solve()