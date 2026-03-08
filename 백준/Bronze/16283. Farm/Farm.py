# Gemini 3 Pro
import sys

def solve():
    input = sys.stdin.readline
    
    try:
        line = input().split()
        if not line: return
        a, b, n, w = map(int, line)
    except ValueError:
        return

    # Case 1: a와 b가 같을 때 (0으로 나누기 방지)
    if a == b:
        # 사료 총량이 딱 맞아떨어지는 경우
        if w == a * n:
            # 전체가 2마리면 (양 1마리, 염소 1마리) 경우의 수 딱 1개뿐
            if n == 2:
                print("1 1")
            # 3마리 이상이면 (1, n-1), (2, n-2) 등 해가 2개 이상이므로 -1
            else:
                print("-1")
        # 사료 총량이 맞지 않으면 해가 없음
        else:
            print("-1")
            
    # Case 2: a와 b가 다를 때 (일반적인 연립방정식 풀이)
    else:
        numerator = w - (b * n)
        denominator = a - b
        
        # 나머지가 0이어야 온전한 마릿수(정수)가 나옴
        if numerator % denominator == 0:
            x = numerator // denominator
            y = n - x
            
            # 조건: 양과 염소 모두 1마리 이상이어야 함
            if x >= 1 and y >= 1:
                print(f"{x} {y}")
            else:
                print("-1")
        else:
            # 나누어 떨어지지 않으면 해가 없는 것
            print("-1")

if __name__ == '__main__':
    solve()