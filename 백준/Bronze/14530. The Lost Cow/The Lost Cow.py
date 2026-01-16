# GPT 5.1
x, y = map(int, input().split())

distance = 0
cur = x
step = 1     # 처음 이동 거리는 1
sign = 1     # 오른쪽 이동(+)부터 시작

while True:
    next_pos = x + sign * step

    # 만약 현재 이동 구간에 Bessie가 포함되면
    if min(cur, next_pos) <= y <= max(cur, next_pos):
        distance += abs(cur - y)
        break

    # 그렇지 않으면 전체 구간 이동
    distance += abs(cur - next_pos)

    # 다음 단계 준비
    cur = next_pos
    step *= 2
    sign *= -1

print(distance)