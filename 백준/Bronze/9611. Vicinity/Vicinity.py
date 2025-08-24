# Gemini 2.5 Pro
import sys

# 두 점 사이의 거리의 제곱을 계산하는 함수
# 제곱근 계산을 피하여 부동소수점 오차를 줄이고 계산 속도를 높입니다.
def get_distance_squared(p1, p2):
    """
    두 점 (x1, y1)과 (x2, y2) 사이의 유클리드 거리의 제곱을 반환합니다.
    
    Args:
        p1 (tuple): 첫 번째 점의 (x, y) 좌표.
        p2 (tuple): 두 번째 점의 (x, y) 좌표.
        
    Returns:
        int: 두 점 사이의 거리의 제곱.
    """
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

# 빠른 입력을 위해 sys.stdin.readline 사용
input = sys.stdin.readline

# 점의 개수 n 입력
try:
    n = int(input())
except (ValueError, IndexError):
    n = 0

# n개의 점 좌표를 리스트에 저장
points = []
for _ in range(n):
    try:
        x, y = map(int, input().split())
        points.append((x, y))
    except (ValueError, IndexError):
        # 잘못된 입력이 들어올 경우를 대비
        continue

# 테스트 케이스의 수 t 입력
try:
    t = int(input())
except (ValueError, IndexError):
    t = 0

# t개의 테스트 케이스 처리
for _ in range(t):
    try:
        # 기준점의 인덱스 i와 근접 거리 dv 입력
        i, dv = map(int, input().split())
        
        # 문제의 인덱스는 1부터 시작하므로, 0부터 시작하는 리스트 인덱스로 변환
        target_point_index = i - 1
        
        # 인덱스가 유효한 범위 내에 있는지 확인
        if not (0 <= target_point_index < len(points)):
            print(0)
            continue
            
        target_point = points[target_point_index]
        
        # 거리의 제곱과 비교할 값이므로 dv도 제곱해줌
        dv_squared = dv * dv
        
        # 근접 거리에 있는 점의 개수를 셀 변수
        vicinity_count = 0
        
        # 모든 점을 순회하며 기준점과의 거리를 확인
        for point in points:
            # 거리의 제곱이 dv의 제곱보다 작거나 같으면 근접한 것으로 판단
            if get_distance_squared(target_point, point) <= dv_squared:
                vicinity_count += 1
        
        # 결과 출력 (자기 자신은 항상 포함되므로, 1을 빼서 제외합니다)
        print(vicinity_count - 1)

    except (ValueError, IndexError):
        # 잘못된 테스트 케이스 입력 처리
        print(0)
        continue