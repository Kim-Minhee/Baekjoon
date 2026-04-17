# Gemini 3.1 Pro
import sys

def solve():
    # 입력 속도를 높이기 위해 sys.stdin.read 사용
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    passports = input_data[1:]
    
    # 중복을 제거하면서 조건에 맞는 번호만 담을 Set 생성
    matched_rooms = set()
    
    for p in passports:
        num = int(p)
        # 여권 번호가 1 이상 N 이하인 경우에만 일치 가능
        if 1 <= num <= n:
            matched_rooms.add(num)
            
    # 고유한 일치 가능 방의 개수 출력
    print(len(matched_rooms))

if __name__ == "__main__":
    solve()