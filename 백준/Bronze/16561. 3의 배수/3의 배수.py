# Gemini 3 Pro
import sys

def solve():
    # 입력 받기
    input_data = sys.stdin.readline().strip()
    if not input_data:
        return
    
    n = int(input_data)
    
    # n을 3으로 나눈 몫을 구함
    N = n // 3
    
    # 조합 공식 (N-1)C2 계산
    # n이 9 미만(예: 3, 6)이어서 N이 1이나 2가 되는 경우,
    # 자연스럽게 분자가 0 이하가 되어 계산 결과가 0이 됩니다.
    if N < 3:
        print(0)
    else:
        answer = (N - 1) * (N - 2) // 2
        print(answer)

if __name__ == "__main__":
    solve()