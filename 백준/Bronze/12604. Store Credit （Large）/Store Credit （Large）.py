# Gemini 3 Pro
import sys

# 대량의 입력을 가장 빠르게 처리하기 위해 sys.stdin.read().split() 사용
def solve():
    """
    Store Credit (Large) 문제 해결 함수
    I <= 2000 이므로 O(I^2) 알고리즘은 위험합니다.
    딕셔너리를 사용하여 O(I) 시간 복잡도로 해결합니다.
    """
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        # 첫 번째 토큰: 테스트 케이스 수 N
        num_test_cases = int(next(iterator))
        
        for i in range(1, num_test_cases + 1):
            # C: 크레딧 총액
            C = int(next(iterator))
            # I: 아이템 개수
            I = int(next(iterator))
            
            # 아이템 가격 리스트 파싱
            prices = []
            for _ in range(I):
                prices.append(int(next(iterator)))
            
            # 빠른 검색을 위한 딕셔너리 생성
            # Key: 가격, Value: 1-based 인덱스
            seen_prices = {}
            
            # 리스트를 한 번만 순회하며 짝을 찾습니다. (O(I))
            for idx, price in enumerate(prices):
                # 현재 아이템(price)과 합쳐서 C가 되는 값(target)을 찾음
                target = C - price
                
                # target 가격이 이미 딕셔너리에 있다면, 정답을 찾은 것입니다.
                if target in seen_prices:
                    # seen_prices에 저장된 인덱스가 항상 현재 인덱스(idx)보다 앞에 있음
                    # 문제 요구사항: 작은 인덱스 먼저 출력 (1-based index)
                    index1 = seen_prices[target]
                    index2 = idx + 1 
                    print(f"Case #{i}: {index1} {index2}")
                    break
                
                # 아직 짝을 못 찾았다면 현재 아이템 정보를 저장합니다.
                # 같은 가격의 물건이 여러 개일 경우, 가장 먼저 나온 인덱스를 유지해도 무방합니다.
                # (어차피 짝이 되는 순간 그 시점의 인덱스와 결합되므로)
                if price not in seen_prices:
                    seen_prices[price] = idx + 1
                    
    except StopIteration:
        pass

if __name__ == "__main__":
    solve()