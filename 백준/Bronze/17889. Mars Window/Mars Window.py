# Gemini 3.1 Pro
import sys

def solve():
    # 입력값을 정수로 변환합니다.
    y = int(sys.stdin.read().strip())
    
    # 2018년을 기준으로 13년마다 동일한 패턴이 반복됩니다.
    # 목표 연도가 주기 내에서 몇 번째에 위치하는지 계산합니다.
    offset = (y - 2018) % 13
    
    # 발사가 가능한 오프셋 집합
    if offset in (0, 2, 4, 6, 8, 11):
        print("yes")
    else:
        print("no")

if __name__ == '__main__':
    solve()