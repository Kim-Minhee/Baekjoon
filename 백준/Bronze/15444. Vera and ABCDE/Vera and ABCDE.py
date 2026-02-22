# GPT 5
import sys
input = sys.stdin.readline

# 각 문자에 대한 블록 정의
blocks = {
    'A': [
        "***",
        "*.*",
        "***",
        "*.*",
        "*.*"
    ],
    'B': [
        "***",
        "*.*",
        "***",
        "*.*",
        "***"
    ],
    'C': [
        "***",
        "*..",
        "*..",
        "*..",
        "***"
    ],
    'D': [
        "***",
        "*.*",
        "*.*",
        "*.*",
        "***"
    ],
    'E': [
        "***",
        "*..",
        "***",
        "*..",
        "***"
    ]
}

N = int(input().strip())
S = input().strip()

# 결과 5줄 준비
result = [""] * 5

# 문자 하나씩 처리
for ch in S:
    for i in range(5):
        result[i] += blocks[ch][i]

# 출력
for line in result:
    print(line)