# GPT 5
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    s, num = input().split()
    num = int(num)
    
    # 표기법1
    col1 = ord(s[0]) - ord('A') + 1
    row1 = int(s[1])
    
    # 표기법2
    row2 = (num - 1) // 8 + 1
    col2 = (num - 1) % 8 + 1
    
    # 색 비교
    if (row1 + col1) % 2 == (row2 + col2) % 2:
        print("YES")
    else:
        print("NO")