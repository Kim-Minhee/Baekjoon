# Gemini 3 Pro
import sys
input = sys.stdin.readline

def solve():
    try:
        line = input().strip()
        if not line: return
        n = int(line)
        
        # 1. 일단 1을 더합니다.
        next_num = n + 1
        
        # 2. 숫자를 문자열로 바꾸고, '0'을 모두 '1'로 바꿉니다.
        # 0이 없으면 아무 변화도 일어나지 않으므로 안전합니다.
        ans = str(next_num).replace('0', '1')
        
        print(ans)
    except ValueError:
        return

if __name__ == "__main__":
    solve()