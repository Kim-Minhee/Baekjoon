# Gemini 3.1 Pro
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    # 입력값을 실수로 읽은 뒤 100을 곱해 센트 단위(정수)로 변환합니다.
    # round()를 써야 부동소수점 오차를 완벽하게 차단할 수 있습니다.
    pt = round(float(input_data[0]) * 100)
    p1 = round(float(input_data[1]) * 100)
    p2 = round(float(input_data[2]) * 100)
    
    found = False
    
    # 피타(x)의 개수를 0개부터 가능한 최대 개수까지 늘려가며 확인합니다.
    max_pitas = pt // p1
    
    for x in range(max_pitas + 1):
        remaining_profit = pt - (x * p1)
        
        # 남은 수익이 피자 수익(p2)으로 나누어 떨어지면 정답을 찾은 것입니다!
        if remaining_profit % p2 == 0:
            y = remaining_profit // p2
            print(f"{x} {y}")
            found = True
            
    # 가능한 조합이 단 하나도 없었다면 none 출력
    if not found:
        print("none")

if __name__ == '__main__':
    solve()