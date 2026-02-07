# GPT 5.1
import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))

# 0이 아닌 값들의 (인덱스, 값)
known = [(i, arr[i]) for i in range(10) if arr[i] != 0]

i, A = known[0]
j, B = known[1]

# d가 정수인지 확인
if (B - A) % (j - i) != 0:
    print(-1)
    exit()

d = (B - A) // (j - i)

# 첫 항 계산
a0 = A - d * i

# 전체 수열 생성
result = [a0 + d * k for k in range(10)]

# 기존 값들과 일치하는지 검증
for idx, val in known:
    if result[idx] != val:
        print(-1)
        exit()

print(' '.join(map(str, result)))