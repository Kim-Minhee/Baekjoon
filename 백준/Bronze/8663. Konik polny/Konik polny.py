# GPT 4o
x, s = map(int, input().split())

jumps = 0
distance = 0
jump_length = s

while distance < x and jump_length > 1:
    distance += jump_length
    jump_length //= 2
    jumps += 1

# 남은 거리만큼 1짜리 점프를 더함
if distance < x:
    jumps += (x - distance)

print(jumps)