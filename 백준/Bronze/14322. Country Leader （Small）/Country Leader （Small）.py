# Gemini 3 Pro
import sys

# 입력을 빠르게 처리하기 위해 sys.stdin.readline 사용
input = sys.stdin.readline

def count_unique_chars(name):
    """
    이름에서 공백을 제외한 서로 다른 알파벳 대문자의 개수를 반환합니다.
    """
    unique_chars = set()
    for char in name:
        # 대문자 알파벳인 경우만 집합에 추가 (공백 무시)
        if 'A' <= char <= 'Z':
            unique_chars.add(char)
    return len(unique_chars)

def solve():
    """
    각 테스트 케이스마다 리더를 선출하여 출력합니다.
    조건 1: 서로 다른 알파벳 개수가 많은 사람이 리더
    조건 2: 개수가 같으면 사전 순으로 앞서는 사람이 리더
    """
    try:
        # 첫 줄: 테스트 케이스의 개수 T
        line = input().strip()
        if not line:
            return
        T = int(line)

        for i in range(1, T + 1):
            # 시민의 수 N
            line = input().strip()
            if not line:
                break
            N = int(line)
            
            leader_name = ""
            max_unique_count = -1
            
            for _ in range(N):
                name = input().strip()
                
                # 현재 이름의 고유 문자 개수 계산
                current_count = count_unique_chars(name)
                
                # 리더 갱신 로직
                if current_count > max_unique_count:
                    # 1. 개수가 더 많으면 무조건 리더 교체
                    leader_name = name
                    max_unique_count = current_count
                elif current_count == max_unique_count:
                    # 2. 개수가 같으면 사전 순으로 더 빠른(작은) 이름 선택
                    if name < leader_name:
                        leader_name = name
                        
            print(f"Case #{i}: {leader_name}")

    except ValueError:
        pass

if __name__ == "__main__":
    solve()