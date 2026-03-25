# GPT 5
import sys
input = sys.stdin.readline

N = int(input())
X = list(map(int, input().split()))

M = int(input())
A = list(map(int, input().split()))

for a in A:
    i = a - 1  # 0-index
    
    # 1. 골인 지점이면 이동 불가
    if X[i] == 2019:
        continue
    
    # 2. 다음 칸에 말이 있는지 확인
    if i < N - 1 and X[i + 1] == X[i] + 1:
        continue
    
    # 3. 이동
    X[i] += 1

# 출력
for x in X:
    print(x)