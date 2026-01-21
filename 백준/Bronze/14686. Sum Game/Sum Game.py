# Gemini 3 Pro
import sys

def solve():
    # 입력 속도 향상
    input = sys.stdin.readline
    
    # 총 일수 N
    n = int(input())
    
    # 두 팀의 점수 리스트
    swifts = list(map(int, input().split()))
    semaphores = list(map(int, input().split()))
    
    sum_swifts = 0
    sum_semaphores = 0
    k = 0
    
    # 1일부터 n일까지 점수를 누적하며 비교
    for i in range(n):
        sum_swifts += swifts[i]
        sum_semaphores += semaphores[i]
        
        # 누적 점수가 같을 때마다 K를 갱신 (마지막 날을 구해야 하므로)
        if sum_swifts == sum_semaphores:
            k = i + 1
            
    print(k)

if __name__ == "__main__":
    solve()