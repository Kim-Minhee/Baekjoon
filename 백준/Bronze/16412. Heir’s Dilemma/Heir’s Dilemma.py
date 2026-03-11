# Gemini 3 Pro
import sys
from itertools import permutations

def solve():
    # 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data: 
        return
    L, H = map(int, input_data)
    
    count = 0
    
    # '1'부터 '9'까지의 문자 중 6개를 뽑아 나열하는 모든 순열 생성
    for p in permutations('123456789', 6):
        # 튜플 형태인 p (예: ('1', '2', '3', '8', '6', '4'))를 문자열로 합치고 정수로 변환
        num = int("".join(p))
        
        # 1. 범위 조건 확인
        if L <= num <= H:
            # 2. 각 자리의 숫자로 모두 나누어 떨어지는지 확인
            # all()을 사용하여 하나라도 나누어 떨어지지 않으면 False 반환
            if all(num % int(d) == 0 for d in p):
                count += 1
                
    print(count)

if __name__ == '__main__':
    solve()