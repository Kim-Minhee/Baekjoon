# Gemini 3 Pro
import sys

# 입력을 빠르게 처리하기 위해 sys.stdin.readline 사용
input = sys.stdin.readline

def solve():
    """
    백준 14648번: 쿼리 맛보기
    주어진 수열에 대해 구간 합 계산 및 원소 교환을 수행하는 쿼리 문제입니다.
    """
    try:
        # N: 수열 길이, q: 쿼리 개수
        line1 = input().split()
        if not line1:
            return
        n, q = map(int, line1)
        
        # 수열 입력
        # 인덱스 계산 편의를 위해 0-based index로 변환해서 사용합니다.
        arr = list(map(int, input().split()))
        
        for _ in range(q):
            query = list(map(int, input().split()))
            
            # 쿼리 타입 (1 또는 2)
            q_type = query[0]
            
            if q_type == 1:
                # 쿼리 1: [a, b] 구간 합 출력 후 swap(a, b)
                a, b = query[1], query[2]
                
                # 1-based index -> 0-based index
                idx_a, idx_b = a - 1, b - 1
                
                # 구간 합 계산 (sum 함수와 슬라이싱 활용)
                # 슬라이싱 범위: arr[idx_a : idx_b + 1]
                section_sum = sum(arr[idx_a : idx_b + 1])
                print(section_sum)
                
                # 원소 교환 (Swap)
                arr[idx_a], arr[idx_b] = arr[idx_b], arr[idx_a]
                
            elif q_type == 2:
                # 쿼리 2: [a, b] 합 - [c, d] 합 출력
                a, b, c, d = query[1], query[2], query[3], query[4]
                
                idx_a, idx_b = a - 1, b - 1
                idx_c, idx_d = c - 1, d - 1
                
                sum1 = sum(arr[idx_a : idx_b + 1])
                sum2 = sum(arr[idx_c : idx_d + 1])
                
                print(sum1 - sum2)

    except ValueError:
        pass

if __name__ == "__main__":
    solve()