# Gemini 3.1 Pro
import sys

def solve():
    # 입력 데이터를 한 번에 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    
    times = []
    distances = []
    
    idx = 1
    for _ in range(n):
        times.append(int(input_data[idx]))
        distances.append(int(input_data[idx+1]))
        idx += 2
        
    max_speed = 0
    
    # 1번 인덱스부터 이전 기록과 비교하여 평균 속도를 계산합니다.
    for i in range(1, n):
        dt = times[i] - times[i-1]      # 걸린 시간
        dd = distances[i] - distances[i-1]  # 이동한 거리
        
        # 확실하게 도달한 최대 '정수' 속도를 요구하므로 
        # 소수점 이하를 버리는 몫(//) 연산자를 사용합니다.
        speed = dd // dt
        
        # 최댓값 갱신
        if speed > max_speed:
            max_speed = speed
            
    print(max_speed)

if __name__ == "__main__":
    solve()