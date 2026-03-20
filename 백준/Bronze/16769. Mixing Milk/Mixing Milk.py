# Gemini 3.1 Pro
import sys

def solve():
    # 입력 데이터를 한 번에 모두 읽어옵니다.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    # c: 각 양동이의 최대 용량(capacity)
    # m: 각 양동이에 현재 들어있는 우유의 양(milk)
    c = [int(input_data[0]), int(input_data[2]), int(input_data[4])]
    m = [int(input_data[1]), int(input_data[3]), int(input_data[5])]
    
    # 100번 우유 붓기 진행
    for i in range(100):
        from_bucket = i % 3        # 붓는 양동이 (0, 1, 2 순환)
        to_bucket = (i + 1) % 3    # 받는 양동이 (1, 2, 0 순환)
        
        # 실제로 이동할 우유의 양 계산 (둘 중 최솟값)
        pour_amt = min(m[from_bucket], c[to_bucket] - m[to_bucket])
        
        # 우유 양 업데이트
        m[from_bucket] -= pour_amt
        m[to_bucket] += pour_amt
        
    # 결과 출력
    for milk in m:
        print(milk)

if __name__ == '__main__':
    solve()