# Gemini 3.1 Pro
import sys

def solve():
    # 입력을 한 줄씩 읽어와 정수 리스트로 변환합니다.
    state_u = list(map(int, sys.stdin.readline().split()))
    u_state = list(map(int, sys.stdin.readline().split()))
    
    # 1. 두 팀의 키를 내림차순(큰 순서대로)으로 정렬합니다.
    state_u.sort(reverse=True)
    u_state.sort(reverse=True)
    
    # 2. zip을 이용해 같은 등수의 선수끼리 짝을 짓고, 
    # State U 선수가 더 클 때만 1을 더해 총합(sum)을 구합니다.
    count = sum(1 for s, u in zip(state_u, u_state) if s > u)
    
    print(count)

if __name__ == '__main__':
    solve()