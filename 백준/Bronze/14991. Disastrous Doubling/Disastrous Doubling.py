# Gemini 3 Pro
import sys

def solve():
    # 빠른 입력을 위해 sys.stdin.read 사용
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    # 첫 번째 값은 N
    iterator = iter(input_data)
    try:
        N = int(next(iterator))
    except StopIteration:
        return

    # 나머지 N개의 b_i 값을 리스트로 변환 필요 없이 반복문에서 처리
    # (메모리 절약을 위해 iterator 그대로 사용)
    
    MOD = 10**9 + 7
    
    # 임계값 설정: b_i의 최대가 2^60이므로, 그보다 조금 큰 2^61 정도로 설정
    # 이 값을 넘으면 "무한대"로 취급 (절대 부족해질 일 없음)
    LIMIT = 2**62 
    
    cur_val = 1    # 실제 값 (에러 체크용)
    cur_mod = 1    # 나머지 값 (정답 출력용)
    is_infinite = False # 실제 값이 LIMIT를 넘었는지 여부

    for _ in range(N):
        b = int(next(iterator))
        
        # 1. 박테리아 2배 증식
        cur_mod = (cur_mod * 2) % MOD
        
        if not is_infinite:
            cur_val *= 2
            # 임계치를 넘으면 무한대 모드로 전환
            if cur_val > LIMIT:
                is_infinite = True
        
        # 2. 실험에 b마리 사용 (빼기)
        # 모듈러 연산에서 뺄셈은 음수가 될 수 있으므로 + MOD 처리
        cur_mod = (cur_mod - (b % MOD) + MOD) % MOD
        
        if not is_infinite:
            cur_val -= b
            # 박테리아가 부족하면 에러
            if cur_val < 0:
                print("error")
                return
        # is_infinite 상태라면:
        # 현재 값(> 2^62) - b(<= 2^60) 은 여전히 매우 큰 양수이므로
        # 별도의 체크나 갱신이 필요 없음 (계속 infinite 상태 유지)

    # 모든 실험이 끝난 후 나머지 값 출력
    print(cur_mod)

if __name__ == "__main__":
    solve()