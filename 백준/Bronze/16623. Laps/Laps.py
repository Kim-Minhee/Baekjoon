# Gemini 3 Pro
import sys

def solve():
    # 입력 데이터를 한 번에 모두 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    # N: 트랙의 길이, M: 기록한 위치의 개수
    N = int(input_data[0])
    M = int(input_data[1])
    
    # 기록된 위치 리스트
    positions = [int(x) for x in input_data[2:]]
    
    laps = 0
    current_pos = 0  # 베서니는 항상 0에서 출발합니다.
    
    for p in positions:
        # 현재 위치가 이전 위치보다 작다면 출발선을 지나친 것 (1바퀴 추가)
        if p < current_pos:
            laps += 1
        # 다음 비교를 위해 현재 위치를 업데이트
        current_pos = p
        
    print(laps)

if __name__ == '__main__':
    solve()