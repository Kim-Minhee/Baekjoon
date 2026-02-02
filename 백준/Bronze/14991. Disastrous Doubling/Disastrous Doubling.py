# GPT 5.1
import sys
input = sys.stdin.readline

MOD = 10**9 + 7

n = int(input().strip())
b = list(map(int, input().split()))

current = 1  # 시작 박테리아 수

for bi in b:
    # 매 실험 시작 전에 2배로 증가
    current *= 2

    # 실험에 필요한 bi만큼 사용
    if current < bi:
        print("error")
        sys.exit(0)

    current -= bi

# 마지막 실험 후 남은 박테리아(mod)
print(current % MOD)