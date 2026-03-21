# Gemini 3.1 Pro
import sys

def solve():
    # 입력 데이터를 한 번에 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    
    # 1부터 1000까지의 시간을 기록할 타임라인 배열 (여유 있게 1001칸 생성)
    timeline = [0] * 1001
    
    idx = 1
    for _ in range(n):
        s = int(input_data[idx])
        t = int(input_data[idx+1])
        b = int(input_data[idx+2])
        idx += 3
        
        # 소가 젖을 짜는 시간 동안 필요한 양동이 개수를 타임라인에 누적
        for i in range(s, t):
            timeline[i] += b
            
    # 타임라인 중 동시에 가장 많이 사용된 양동이의 개수 출력
    print(max(timeline))

if __name__ == '__main__':
    solve()