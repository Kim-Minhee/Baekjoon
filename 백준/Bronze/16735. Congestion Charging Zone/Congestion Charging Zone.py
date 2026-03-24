# Gemini 3.1 Pro
import sys

def solve():
    # 입력 데이터를 한 번에 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    times = input_data[1:]
    
    valid_minutes = []
    
    # 1. 시간 데이터를 '분' 단위로 변환하고 혼잡 시간대(CP) 필터링
    # CP: 06:30(390분) ~ 19:00(1140분)
    for t in times:
        h, m = map(int, t.split(':'))
        total_mins = h * 60 + m
        
        if 390 <= total_mins <= 1140:
            valid_minutes.append(total_mins)
            
    # 혼잡 시간대에 발견된 기록이 아예 없다면 요금은 0원
    if not valid_minutes:
        print(0)
        return
        
    # 2. 처음 발견된 시간과 마지막 발견된 시간 찾기
    first_seen = min(valid_minutes)
    last_seen = max(valid_minutes)
    
    # 3. 표에 따른 요금 계산
    # 기준점: 10:00(600분), 16:00(960분)
    if first_seen <= 600:
        if last_seen <= 960:
            print(24000)
        else:
            print(36000)
    else:  # 처음 발견된 시간이 10:01(601분) 이후인 경우
        if last_seen <= 960:
            print(16800)
        else:
            print(24000)

if __name__ == '__main__':
    solve()