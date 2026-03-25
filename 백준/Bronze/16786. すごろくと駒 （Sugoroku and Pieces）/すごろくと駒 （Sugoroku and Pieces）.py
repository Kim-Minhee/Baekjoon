# Gemini 3.1 Pro
import sys

def solve():
    # 입력 데이터를 한 번에 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    
    # 말들의 위치 배열 (1번 말부터 N번 말까지)
    # 인덱스 계산을 편하게 하기 위해 파이썬의 0-based 인덱스를 사용합니다.
    positions = [int(x) for x in input_data[1 : n + 1]]
    
    m = int(input_data[n + 1])
    
    # 이동시킬 말의 번호 배열
    moves = [int(x) for x in input_data[n + 2 : n + 2 + m]]
    
    # 조작 시작
    for piece_num in moves:
        idx = piece_num - 1  # 배열 인덱스는 0부터 시작하므로 1을 빼줍니다.
        
        # 1. 이미 도착점(2019)에 있는 경우 이동 불가
        if positions[idx] == 2019:
            continue
            
        # 2. 바로 다음 번호의 말이 내 앞 칸을 막고 있는 경우 이동 불가
        # (단, 내가 마지막 번호의 말이라면 다음 말이 없으므로 이 검사를 건너뜁니다)
        if idx + 1 < n and positions[idx] + 1 == positions[idx + 1]:
            continue
            
        # 위 두 조건에 모두 걸리지 않았다면 1칸 전진!
        positions[idx] += 1
        
    # 모든 조작이 끝난 후 각 말의 위치를 출력
    for pos in positions:
        print(pos)

if __name__ == '__main__':
    solve()