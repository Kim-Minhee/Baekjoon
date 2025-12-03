# Gemini 3 Pro
import sys

def solve():
    """
    GBus Count 문제 해결 함수 (Large Dataset 대응)
    차분 배열(Difference Array)과 누적 합(Prefix Sum)을 사용하여
    O(Max_City) 시간 복잡도로 가장 효율적으로 해결합니다.
    """
    # 모든 입력을 한 번에 읽어서 공백 단위로 분리 (입력 포맷 예외 처리 용이)
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        T_str = next(iterator)
        T = int(T_str)
        
        for i in range(1, T + 1):
            N = int(next(iterator))
            
            # 버스 범위 정보 파싱
            buses = []
            max_city_index = 0
            
            # A1 B1 A2 B2 ... 순서로 2N개의 숫자가 들어옴
            for _ in range(N):
                start = int(next(iterator))
                end = int(next(iterator))
                buses.append((start, end))
                # 배열 크기를 결정하기 위해 가장 큰 도시 번호를 찾습니다.
                max_city_index = max(max_city_index, end)
            
            # 쿼리 정보 파싱
            P = int(next(iterator))
            queries = []
            for _ in range(P):
                city = int(next(iterator))
                queries.append(city)
                # 쿼리에 등장하는 도시가 버스 범위보다 클 수도 있으므로 확인
                max_city_index = max(max_city_index, city)
            
            # 1. 차분 배열(Difference Array) 생성
            # 크기는 max_city_index + 2 (인덱스 초과 방지 및 1-based indexing 고려)
            count_array = [0] * (max_city_index + 2)
            
            # 2. 범위 마킹 (O(N))
            # [Start, End] 구간에 1을 더한다 -> Start에 +1, End+1에 -1
            for start, end in buses:
                count_array[start] += 1
                count_array[end + 1] -= 1
            
            # 3. 누적 합(Prefix Sum) 계산 (O(Max_City))
            # 앞에서부터 누적해서 더하면 각 도시별 실제 버스 수가 됩니다.
            current_count = 0
            for j in range(len(count_array)):
                current_count += count_array[j]
                count_array[j] = current_count
            
            # 4. 결과 추출 (O(P))
            result = []
            for q in queries:
                # 미리 계산된 배열에서 값만 가져오면 됨 (O(1))
                result.append(str(count_array[q]))
            
            print(f"Case #{i}: {' '.join(result)}")
            
    except StopIteration:
        pass

if __name__ == "__main__":
    solve()