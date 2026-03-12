# Gemini 3 Pro
import sys

def solve():
    input = sys.stdin.readline
    
    # 암호문(msg)과 원문(crib) 입력 (개행 문자 제거)
    msg = input().strip()
    crib = input().strip()
    
    if not msg or not crib:
        return
        
    N = len(msg)
    L = len(crib)
    
    valid_positions = 0
    
    # Crib을 매칭할 수 있는 모든 시작 위치 탐색
    for i in range(N - L + 1):
        
        # msg의 i번째부터 L만큼 잘라낸 부분 문자열과 crib을 1:1로 비교
        # any()는 조건이 하나라도 True면 즉시 True를 반환하고 검사를 멈춤 (Short-circuit)
        # 즉, 같은 위치에 같은 글자가 하나라도 있으면 invalid한 위치임
        if not any(m == c for m, c in zip(msg[i : i+L], crib)):
            valid_positions += 1
            
    print(valid_positions)

if __name__ == '__main__':
    solve()