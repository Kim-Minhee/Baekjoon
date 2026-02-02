import sys
input = sys.stdin.readline

def solve():
    try:
        line1 = input().strip()
        if not line1: return
        N = int(line1)
        
        # B 리스트 입력
        # 입력 데이터가 매우 많을 수 있으므로 sys.stdin.read()가 더 빠를 수 있지만
        # 질문자님 스타일대로 input().split() 유지
        B = list(map(int, input().split()))
    except ValueError:
        return

    # 두 개의 변수로 분리
    cur_mod = 1        # 정답 출력용 (나머지 값)
    cur_val = 1        # 에러 체크용 (실제 값)
    
    MOD = 1000000007
    LIMIT = 2**61      # 충분히 큰 값 (문제의 bi 최대값인 2^60보다 큼)
    is_infinite = False # cur_val이 LIMIT를 넘었는지 여부

    for hour in range(N):
        # 1. 박테리아 2배 증식
        cur_mod = (cur_mod * 2) % MOD
        
        # 실제 값은 LIMIT를 넘지 않았을 때만 계산
        if not is_infinite:
            cur_val *= 2
            if cur_val > LIMIT:
                is_infinite = True
        
        need_b = B[hour]
        
        # 2. 박테리아 사용 (검증)
        # 무한대 상태면 무조건 충분하므로 체크할 필요 없음
        if not is_infinite:
            if cur_val < need_b:
                print('error')
                return
            cur_val -= need_b
            
        # 정답용 변수 계산 (뺄셈 후 음수 방지를 위해 + MOD)
        cur_mod = (cur_mod - (need_b % MOD) + MOD) % MOD

    # 에러 없이 끝났다면 나머지 출력
    print(cur_mod)

if __name__ == "__main__":
    solve()