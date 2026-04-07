# Gemini 3.1 Pro
import sys
input = sys.stdin.readline

def solve():
    N = int(input().strip())
    
    # shells[i]: 현재 i번 위치에 놓인 껍데기의 '최초 출발 위치(1, 2, 3)'
    # 직관적인 인덱스 사용을 위해 0번 인덱스는 비워둡니다.
    shells = [0, 1, 2, 3]
    
    # scores[i]: 조약돌이 최초에 i번 위치에 있었을 경우 얻게 되는 누적 점수
    scores = [0, 0, 0, 0]
    
    for _ in range(N):
        a, b, g = map(int, input().split())
        
        # 1. a번 위치와 b번 위치의 껍데기를 교환합니다. (파이썬의 다중 할당 스왑)
        shells[a], shells[b] = shells[b], shells[a]
        
        # 2. Elsie가 g번 위치를 지목했습니다.
        # 현재 g번 위치에 있는 껍데기의 '최초 출발 번호'를 찾아 그 시나리오에 1점을 더합니다.
        scores[shells[g]] += 1
        
    # 1, 2, 3번 출발 시나리오 중 가장 높은 점수를 출력합니다.
    print(max(scores))

if __name__ == '__main__':
    solve()