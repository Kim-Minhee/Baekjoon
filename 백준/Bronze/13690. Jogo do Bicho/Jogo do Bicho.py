# Gemini 3 Pro
import sys

# 입력을 빠르게 처리하기 위해 sys.stdin.read().split() 사용
def solve():
    """
    Jogo do Bicho (동물 게임) 당첨금 계산 함수
    - 우선순위에 따라 마지막 4자리, 3자리, 2자리, 동물 그룹 일치 여부를 확인합니다.
    """
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    # 동물 그룹을 계산하는 헬퍼 함수
    def get_animal_group(number):
        # 마지막 두 자리만 사용
        two_digits = number % 100
        if two_digits == 0:
            return 25
        # (숫자 - 1) // 4 + 1 공식을 사용하여 1~25 그룹 매핑
        # 예: 01~04 -> 0~3 // 4 -> 0 -> +1 -> 1그룹
        return (two_digits - 1) // 4 + 1

    try:
        while True:
            # V: 배팅 금액 (실수)
            # N: 선택한 숫자, M: 추첨된 숫자
            V = float(next(iterator))
            N = int(next(iterator))
            M = int(next(iterator))
            
            # 종료 조건: 0 0 0 입력 시 중단
            if V == 0.0 and N == 0 and M == 0:
                break
            
            prize = 0.0
            
            # 1. 마지막 4자리 일치 (V x 3000)
            if N % 10000 == M % 10000:
                prize = V * 3000
                
            # 2. 마지막 3자리 일치 (V x 500)
            elif N % 1000 == M % 1000:
                prize = V * 500
                
            # 3. 마지막 2자리 일치 (V x 50)
            elif N % 100 == M % 100:
                prize = V * 50
                
            # 4. 동물 그룹 일치 (V x 16)
            # 마지막 2자리가 같은 그룹에 속하는지 확인
            elif get_animal_group(N) == get_animal_group(M):
                prize = V * 16
            
            # 당첨되지 않음 -> 0.0
            
            # 소수점 2자리까지 출력
            print(f"{prize:.2f}")
            
    except StopIteration:
        pass

if __name__ == "__main__":
    solve()