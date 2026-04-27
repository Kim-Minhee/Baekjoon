# Gemini 3.1 Pro
import sys

def solve():
    # 입력 속도를 높이기 위해 한 번에 통째로 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    # N과 M 값은 사실 더할 필요가 없으므로 건너뜁니다.
    # input_data[0]은 N, input_data[1]은 M
    
    # 배열 A와 B의 원소들은 input_data의 2번 인덱스부터 끝까지 들어있습니다.
    # 어떤 경로로 가든 모든 A 원소와 모든 B 원소를 한 번씩 더하게 되므로,
    # 남아있는 모든 값들의 총합을 구하면 됩니다.
    total_garbage = sum(int(x) for x in input_data[2:])
    
    print(total_garbage)

if __name__ == "__main__":
    solve()