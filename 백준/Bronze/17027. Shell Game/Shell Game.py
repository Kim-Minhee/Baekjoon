# Gemini 3.1 Pro
import sys

def solve():
    # 입력 데이터를 한 번에 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    
    # shells[i]는 현재 i번 위치에 있는 껍데기의 '초기 번호(1, 2, 3)'를 의미합니다.
    # 인덱스를 직관적으로 쓰기 위해 0번 인덱스는 0으로 비워둡니다.
    shells = [0, 1, 2, 3]
    
    # 각 초기 껍데기 번호(1, 2, 3) 밑에 조약돌이 있었을 경우 얻게 되는 점수입니다.
    scores = [0, 0, 0, 0]
    
    idx = 1
    for _ in range(n):
        a = int(input_data[idx])
        b = int(input_data[idx + 1])
        g = int(input_data[idx + 2])
        idx += 3
        
        # 1. a 위치와 b 위치의 껍데기를 교환합니다.
        shells[a], shells[b] = shells[b], shells[a]
        
        # 2. Elsie가 g 위치를 지목했습니다.
        # 현재 g 위치에 있는 껍데기(shells[g])에 조약돌이 들어있다면 점수를 얻습니다.
        scores[shells[g]] += 1
        
    # 1, 2, 3번 껍데기 중 가장 높은 점수를 출력합니다.
    print(max(scores[1:]))

if __name__ == '__main__':
    solve()