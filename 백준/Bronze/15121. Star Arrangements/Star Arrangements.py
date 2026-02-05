# Gemini 3 Pro
import sys

def solve():
    # 입력 받기
    try:
        line = sys.stdin.readline()
        if not line:
            return
        S = int(line.strip())
    except ValueError:
        return

    # 출력 헤더
    print(f"{S}:")

    # x는 첫 번째 줄의 별 개수입니다.
    # "S-by-1" (x=1, y=1)은 제외하므로 x는 2부터 시작합니다.
    # "1-by-S" (x=S)는 제외하므로 x는 S 미만까지 반복합니다.
    for x in range(2, S):
        
        # 1. (x, x-1) 패턴 검사 (y가 작은 경우 먼저 출력)
        y = x - 1
        pair_sum = x + y  # 2x - 1
        
        # 짝수 줄인 경우 (x, y, x, y ...) -> 합이 pair_sum의 배수
        if S % pair_sum == 0:
            print(f"{x},{y}")
        # 홀수 줄인 경우 (x, y, ... x) -> (합 - x)가 pair_sum의 배수
        # 단, S-x가 0이면(즉 S==x) 1줄이라는 뜻이므로 제외 (S > x 조건 필요)
        elif (S - x) > 0 and (S - x) % pair_sum == 0:
            print(f"{x},{y}")

        # 2. (x, x) 패턴 검사
        # 모든 줄이 x개. 1줄인 경우(S==x)는 제외해야 하므로 S > x 조건 확인
        if S > x and S % x == 0:
            print(f"{x},{x}")

if __name__ == "__main__":
    solve()