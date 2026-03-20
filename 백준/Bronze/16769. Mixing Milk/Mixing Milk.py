# GPT 5
import sys
input = sys.stdin.readline

# 용량, 현재 우유
c = []
m = []

for _ in range(3):
    ci, mi = map(int, input().split())
    c.append(ci)
    m.append(mi)

# 100번 반복
for i in range(100):
    a = i % 3
    b = (i + 1) % 3
    
    # 옮길 수 있는 양
    pour = min(m[a], c[b] - m[b])
    
    m[a] -= pour
    m[b] += pour

# 출력
for x in m:
    print(x)