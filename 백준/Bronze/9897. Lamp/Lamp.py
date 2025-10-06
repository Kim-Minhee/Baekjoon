# GPT 5
import sys
input = sys.stdin.readline

# 입력
L, G, R = map(int, input().split())

# 각 경비원의 램프 제어 규칙 저장
guards = {}
for _ in range(G):
    name, a0, d = input().split()
    guards[name] = (int(a0), int(d))

# 램프 상태 (False = 꺼짐, True = 켜짐)
lamps = [False] * (L + 1)  # 1-based index 사용

# 순찰 순서에 따라 처리
for _ in range(R):
    name = input().strip()
    a0, d = guards[name]
    # 해당 경비원의 램프 토글
    i = a0
    while i <= L:
        lamps[i] = not lamps[i]
        i += d

# 결과 출력
print(sum(lamps))