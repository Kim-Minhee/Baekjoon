# Gemini 3 Pro
import sys

def solve():
    input = sys.stdin.readline
    
    # x: 거리, k: Kozik 보폭, a: Adrian 보폭
    try:
        line = input().split()
        if not line: return
        x, k, a = map(int, line)
    except ValueError:
        return

    # 나머지를 구함
    rem = x % (k + a)
    
    # 수정된 승리 조건:
    # 나머지가 k보다 "작아야" Kozik이 밟을 수 있음 (0 포함)
    # 나머지가 k와 같으면 Kozik은 밟지 못하고 딱 붙이게 되어 다음 턴인 Adrian이 승리
    if rem < k:
        print(1)
    else:
        print(0)

if __name__ == "__main__":
    solve()