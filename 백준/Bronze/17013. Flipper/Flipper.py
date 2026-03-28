# Gemini 3.1 Pro
import sys

def solve():
    # 1. 입력 문자열을 한 번에 읽어옵니다. (공백 및 줄바꿈 제거)
    seq = sys.stdin.read().strip()
    if not seq:
        return
        
    # 2. H와 V의 총 개수를 세고, 홀수 번인지 짝수 번인지 판별합니다.
    # count() 함수는 C언어 레벨에서 동작하여 매우 빠릅니다.
    h_flips = seq.count('H') % 2
    v_flips = seq.count('V') % 2
    
    # 3. 초기 2x2 격자 상태
    grid = [[1, 2], 
            [3, 4]]
    
    # 4. 가로(가운데 가로선 기준)로 뒤집기: 위아래 행이 통째로 교환됩니다.
    if h_flips:
        grid[0], grid[1] = grid[1], grid[0]
        
    # 5. 세로(가운데 세로선 기준)로 뒤집기: 좌우 열의 위치가 각각 교환됩니다.
    if v_flips:
        grid[0][0], grid[0][1] = grid[0][1], grid[0][0]
        grid[1][0], grid[1][1] = grid[1][1], grid[1][0]
        
    # 6. 최종 결과 출력
    for row in grid:
        print(f"{row[0]} {row[1]}")

if __name__ == '__main__':
    solve()