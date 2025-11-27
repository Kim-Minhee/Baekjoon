# Gemini 3 Pro
import sys

# 입력을 빠르게 처리하기 위해 sys.stdin.readline 사용
input = sys.stdin.readline

# 각 숫자(0부터 9)를 표시하는 데 필요한 세그먼트의 개수
# 인덱스 = 숫자, 값 = 세그먼트 개수
# 0(6), 1(2), 2(5), 3(5), 4(4), 5(5), 6(6), 7(3), 8(7), 9(6)
SEGMENTS_COUNT = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

def calculate_segments(hh: int, mm: int) -> int:
    """
    주어진 시간(hh:mm)을 표시하는 데 필요한 총 세그먼트 개수를 계산합니다.
    """
    # 시간의 두 자릿수 (H1, H2)
    h1 = hh // 10
    h2 = hh % 10
    
    # 분의 두 자릿수 (M1, M2)
    m1 = mm // 10
    m2 = mm % 10
    
    # 각 자릿수의 세그먼트 개수를 합산
    total_segments = (
        SEGMENTS_COUNT[h1] + 
        SEGMENTS_COUNT[h2] + 
        SEGMENTS_COUNT[m1] + 
        SEGMENTS_COUNT[m2]
    )
    return total_segments

def solve():
    """
    N개의 세그먼트를 사용하는 유효한 시간을 찾습니다.
    """
    try:
        # 입력 N (세그먼트의 총 개수)
        line = input().strip()
        if not line:
            # 입력이 없으면 종료
            return
        N = int(line)
        
    except ValueError:
        return

    # 00:00부터 23:59까지 모든 유효한 시간을 순회 (전체 탐색)
    # 총 24 * 60 = 1440회 반복
    for hh in range(24):
        for mm in range(60):
            
            # 현재 시간의 총 세그먼트 개수를 계산
            current_segments = calculate_segments(hh, mm)
            
            # 세그먼트 개수가 N과 일치하면 정답을 찾은 것입니다.
            if current_segments == N:
                # "hh:mm" 형식으로 출력
                # f-string의 :02d를 사용하여 항상 두 자리로(예: 9 -> 09) 출력합니다.
                print(f"{hh:02d}:{mm:02d}")
                return # 첫 번째 답을 찾았으므로 프로그램 종료

    # 전체 탐색 후에도 답을 찾지 못했다면 불가능
    print("Impossible")


if __name__ == "__main__":
    solve()