# GPT 4o
import math

# 입력 처리
N, K, M = map(int, input().split())

# 색상 번호는 1부터 시작하므로 인덱스를 맞추기 위해 +1 크기로 초기화
groups = [[] for _ in range(K)]
for i in range(K):
    data = list(map(int, input().split()))
    groups[i] = data[1:]  # 그룹 내 색상 목록만 저장

# 색상별 옷 개수 입력
D = list(map(int, input().split()))
D = [0] + D  # 색상 번호 1부터 시작하므로 인덱스 보정

# 총 세탁 횟수 계산
total_washes = 0
for group in groups:
    clothes = 0
    for color in group:
        clothes += D[color]
    washes = math.ceil(clothes / M)
    total_washes += washes

# 결과 출력
print(total_washes)