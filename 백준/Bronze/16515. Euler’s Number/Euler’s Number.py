# Gemini 3.1 Pro
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])

    e_approx = 1.0  # 1 / 0!
    term = 1.0      # 각 항의 값
    
    for i in range(1, n + 1):
        term /= i  # 이전 항에서 i를 나누면 1 / i! 이 됨
        
        # 항이 너무 작아져서 부동소수점으로 0.0이 되면 더 더할 필요가 없음
        if term == 0.0:
            break
            
        e_approx += term

    # 상대/절대 오차 10^-12 이하를 만족하도록 소수점 12자리까지 출력
    print(f"{e_approx:.12f}")

if __name__ == '__main__':
    solve()