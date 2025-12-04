# Gemini 3 Pro
import sys

# 입력을 빠르게 처리하기 위해 sys.stdin.read().split() 사용
def solve():
    """
    Jeff가 연주할 수 있는 가장 낮은 조화로운 음을 찾는 함수
    범위(H)가 작으므로 Brute Force(완전 탐색)로 해결합니다.
    """
    # 모든 입력을 한 번에 읽어서 공백 단위로 분리
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        # 첫 번째 토큰: 테스트 케이스 수 T
        T_str = next(iterator)
        T = int(T_str)
        
        for i in range(1, T + 1):
            # N: 다른 연주자 수, L: 최소 음, H: 최대 음
            N = int(next(iterator))
            L = int(next(iterator))
            H = int(next(iterator))
            
            # 다른 연주자들의 음을 입력받음
            # 중복된 음은 검사할 필요가 없으므로 set으로 변환하여 최적화
            others = set()
            for _ in range(N):
                others.add(int(next(iterator)))
            
            found_note = None
            
            # Jeff가 연주 가능한 범위 [L, H]를 순회
            # 가장 낮은 음을 찾아야 하므로 L부터 시작하여 오름차순 탐색
            for f in range(L, H + 1):
                is_harmonious = True
                
                # 현재 음 f가 다른 모든 연주자의 음과 조화를 이루는지 확인
                for other_note in others:
                    # 조화 조건:
                    # 1. f가 other_note의 배수이다 (f % other_note == 0)
                    # 2. f가 other_note의 약수이다 (other_note % f == 0)
                    if (f % other_note != 0) and (other_note % f != 0):
                        is_harmonious = False
                        break # 하나라도 조화롭지 않으면 즉시 중단 (Pruning)
                
                # 모든 연주자와 조화롭다면 그게 정답
                if is_harmonious:
                    found_note = f
                    break # 가장 낮은 음을 찾았으므로 탐색 종료
            
            # 결과 출력
            if found_note is not None:
                print(f"Case #{i}: {found_note}")
            else:
                print(f"Case #{i}: NO")
            
    except StopIteration:
        pass

if __name__ == "__main__":
    solve()