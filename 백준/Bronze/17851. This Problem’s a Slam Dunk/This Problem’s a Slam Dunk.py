# GPT 5
import sys
input = sys.stdin.readline

state = list(map(int, input().split()))
ustate = list(map(int, input().split()))

# 내림차순 정렬
state.sort(reverse=True)
ustate.sort(reverse=True)

count = 0

for i in range(5):
    if state[i] > ustate[i]:
        count += 1

print(count)