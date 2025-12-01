# Gemini 3 Pro
import sys

# 입력을 빠르게 처리하기 위해 sys.stdin.readline 사용
input = sys.stdin.readline

def solve():
    """
    기립박수 문제를 해결하는 함수
    S_max가 1000으로 커져도 O(S_max)의 선형 시간 복잡도로 해결하므로
    여전히 매우 효율적입니다.
    """
    try:
        # 첫 줄: 테스트 케이스의 개수 T
        line = input().strip()
        if not line:
            return
        T = int(line)

        for i in range(1, T + 1):
            # 입력: S_max와 관객 분포 문자열
            parts = input().split()
            if not parts:
                break
                
            # S_max는 반복문 범위로도 알 수 있지만 입력 변수로 받아둡니다.
            S_max = int(parts[0])
            people_counts = parts[1]
            
            friends_needed = 0   # 초대한 친구의 수 (필요한 최소 인원)
            current_standing = 0 # 현재 기립해 있는 사람의 수 (친구 포함)
            
            # 수줍음 레벨 k는 0부터 S_max까지입니다.
            # enumerate를 사용하여 (수줍음 레벨, 해당 레벨의 사람 수)를 순회합니다.
            for k, count_char in enumerate(people_counts):
                count = int(count_char)
                
                # 핵심 로직:
                # 수줍음 레벨이 k인 사람이 일어서려면, 내 앞(또는 친구)에 최소 k명이 서 있어야 합니다.
                if current_standing < k:
                    # 부족한 인원만큼 친구를 초대합니다.
                    needed = k - current_standing
                    friends_needed += needed
                    
                    # 초대한 친구들도 기립박수에 동참하므로 현재 서 있는 수에 더합니다.
                    current_standing += needed
                
                # 조건이 충족되었으므로, 수줍음 레벨 k인 원래 관객들도 일어섭니다.
                current_standing += count
            
            # 결과 출력
            print(f"Case #{i}: {friends_needed}")

    except ValueError:
        pass

if __name__ == "__main__":
    solve()