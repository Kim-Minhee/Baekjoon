# Gemini 3 Pro
import sys

def solve():
    input_data = sys.stdin.readline().split()
    if not input_data:
        return
        
    t = int(input_data[0])
    p = int(input_data[1])
    
    # 1. 배터리가 20% 이상 남았을 때
    if p >= 20:
        # 1% 닳는 데 걸린 시간 (일반 모드 기준)
        time_per_percent = t / (100 - p)
        
        # 남은 시간 = (일반 모드로 닳을 시간) + (절전 모드로 닳을 시간)
        normal_time = (p - 20) * time_per_percent
        eco_time = 20 * (time_per_percent * 2)
        
        answer = normal_time + eco_time
        
    # 2. 배터리가 20% 미만 남았을 때
    else:
        # 지금까지 쓴 전체 배터리를 일반 모드 비율로 환산
        # 80%(일반) + (20 - p)%(절전, 2배)
        used_equivalent = 80 + (20 - p) * 2
        
        # 1% 닳는 데 걸린 시간 (일반 모드 기준)
        time_per_percent = t / used_equivalent
        
        # 남은 시간은 모두 절전 모드
        answer = p * (time_per_percent * 2)
        
    # 오차 범위 10^-4 이하를 만족하도록 소수점 6자리까지 넉넉히 출력
    print(f"{answer:.6f}")

if __name__ == '__main__':
    solve()