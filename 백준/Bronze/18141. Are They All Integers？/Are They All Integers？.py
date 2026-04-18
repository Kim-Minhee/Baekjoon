# Gemini 3.1 Pro
import sys
from collections import Counter

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    A = list(map(int, input_data[1:]))
    
    # 원소가 3개 미만이면 뽑을 수 없으므로 조건이 항상 참(vacuously true)이거나
    # 문제의 전제에 따라 예외 처리
    if n < 3:
        print("yes")
        return
        
    # 각 원소의 등장 횟수를 셉니다.
    counts = Counter(A)
    
    # 1. 모든 숫자가 동일한 경우
    if len(counts) == 1:
        print("yes")
        
    # 2. 숫자가 딱 2종류인 경우
    elif len(counts) == 2:
        keys = sorted(counts.keys())
        small, big = keys[0], keys[1]
        
        # 작은 숫자가 n-1개이고, 큰 숫자가 1개이며, 큰 숫자가 작은 숫자의 배수인지 확인
        if counts[small] == n - 1 and counts[big] == 1 and big % small == 0:
            print("yes")
        else:
            print("no")
            
    # 3. 서로 다른 숫자가 3종류 이상인 경우
    else:
        print("no")

if __name__ == "__main__":
    solve()