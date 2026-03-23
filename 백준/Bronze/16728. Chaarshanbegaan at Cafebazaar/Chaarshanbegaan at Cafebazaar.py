# Gemini 3.1 Pro
import sys

def solve():
    input = sys.stdin.readline
    
    # N: 다트를 던진 횟수
    try:
        n = int(input().strip())
    except ValueError:
        return
        
    total_score = 0
    
    # 각 점수 구간의 상한선(d)을 제곱한 값들을 미리 리스트로 만들어 둡니다.
    # d = 10, 30, 50, 70, 90, 110, 130, 150, 170, 190
    # bounds = [100, 900, 2500, 4900, 8100, 12100, 16900, 22500, 28900, 36100]
    bounds = [(10 + 20 * i)**2 for i in range(10)]
    
    for _ in range(n):
        x, y = map(int, input().split())
        
        # 피타고라스의 정리 (루트를 씌우지 않고 제곱 상태로 둡니다)
        d_sq = x**2 + y**2
        
        score = 0
        # 가장 작은 구간부터 확인하여 포함되면 점수를 부여하고 반복을 멈춥니다.
        for i, bound in enumerate(bounds):
            if d_sq <= bound:
                score = 10 - i  # 0번 인덱스면 10점, 1번 인덱스면 9점 ...
                break
                
        total_score += score
        
    print(total_score)

if __name__ == '__main__':
    solve()