# Gemini 3.1 Pro
import sys

def solve():
    # 입력 데이터를 한 번에 모두 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    A = list(map(int, input_data[1:]))
    
    # 펭귄의 위치(인덱스)를 찾습니다. 펭귄은 -1로 표시되어 있습니다.
    penguin_idx = A.index(-1)
    
    # 1. 펭귄 기준 왼쪽에서 가장 깨기 쉬운(비용이 적은) 얼음을 찾습니다.
    min_left = min(A[:penguin_idx])
    
    # 2. 펭귄 기준 오른쪽에서 가장 깨기 쉬운 얼음을 찾습니다.
    min_right = min(A[penguin_idx + 1:])
    
    # 양쪽을 끊어내는 최소 비용의 합을 출력합니다.
    print(min_left + min_right)

if __name__ == "__main__":
    solve()