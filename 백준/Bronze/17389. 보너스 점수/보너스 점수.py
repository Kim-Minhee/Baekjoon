# Gemini 3.1 Pro
import sys

def solve():
    # 입력 데이터를 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    s = input_data[1]
    
    total_score = 0
    bonus_score = 0
    
    # enumerate를 사용하여 인덱스(0부터 시작)와 해당 문자를 동시에 가져옵니다.
    for i, char in enumerate(s):
        if char == 'O':
            base_score = i + 1  # 0번 인덱스는 1번 문제, 1번 인덱스는 2번 문제...
            total_score += base_score + bonus_score
            bonus_score += 1
        else:
            bonus_score = 0  # 틀렸을 경우 보너스 점수 초기화
            
    print(total_score)

if __name__ == '__main__':
    solve()