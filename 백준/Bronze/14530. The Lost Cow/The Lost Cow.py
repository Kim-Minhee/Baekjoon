# Gemini 3 Pro
import sys

# 입력을 빠르게 처리하기 위해 sys.stdin.readline 사용
input = sys.stdin.readline

def solve():
    """
    백준 14530번: The Lost Cow
    Farmer John이 x에서 시작하여 지그재그 패턴(x+1, x-2, x+4...)으로 이동하며
    Bessie(y)를 찾을 때까지의 총 이동 거리를 계산합니다.
    """
    try:
        # x: Farmer John의 시작 위치, y: Bessie의 위치
        line = input().strip()
        if not line:
            return
        x, y = map(int, line.split())
        
        # x와 y가 같다면 이동 거리는 0
        if x == y:
            print(0)
            return

        total_dist = 0
        curr = x        # 현재 위치
        step = 1        # 다음 이동 거리 (초기값 1)
        
        while True:
            # 다음 목표 위치 계산 (x를 기준으로 step만큼 떨어진 곳)
            # step은 1, -2, 4, -8 ... 순서로 변함
            target = x + step
            
            # 현재 이동 경로(curr -> target) 사이에 y가 있는지 확인
            # min(curr, target) <= y <= max(curr, target) 조건을 사용하면 방향 무관하게 확인 가능
            if min(curr, target) <= y <= max(curr, target):
                # 이동 중에 Bessie를 찾음!
                # 현재 위치에서 Bessie까지의 거리만 더하고 종료
                total_dist += abs(curr - y)
                print(total_dist)
                break
            else:
                # Bessie를 못 찾음 -> 목표 위치까지 이동
                # 현재 위치에서 목표 위치까지의 거리 누적
                dist = abs(curr - target)
                total_dist += dist
                
                # 위치 업데이트
                curr = target
                
                # 다음 패턴 준비: 부호 반전(-), 거리 2배(*2)
                step *= -2
                
    except ValueError:
        pass

if __name__ == "__main__":
    solve()