# Gemini 3.1 Pro
import sys

def solve():
    input = sys.stdin.readline
    
    # 첫 줄: 테스트 케이스의 수 T
    try:
        T = int(input().strip())
    except ValueError:
        return
        
    for _ in range(T):
        pos1, pos2 = input().split()
        
        # 표기법 1 (예: "A1") 분해
        # 'A'의 아스키코드는 65이므로, ord('A')를 빼고 1을 더하면 1~8의 숫자로 변환됩니다.
        col1 = ord(pos1[0]) - ord('A') + 1
        row1 = int(pos1[1])
        
        # 표기법 2 (예: "17") 분해
        num = int(pos2)
        # 1부터 시작하는 인덱스를 0부터 시작하도록 1을 뺀 뒤 계산하고 다시 1을 더해줍니다.
        col2 = (num - 1) % 8 + 1
        row2 = (num - 1) // 8 + 1
        
        # 두 좌표의 합이 홀수인지 짝수인지(나머지 2) 비교합니다.
        if (col1 + row1) % 2 == (col2 + row2) % 2:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()