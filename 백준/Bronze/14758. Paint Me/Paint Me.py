# GPT 5.1
import sys
input = sys.stdin.readline

while True:
    n, width, length, height, area, m = map(int, input().split())
    if n == 0 and width == 0 and length == 0 and height == 0 and area == 0 and m == 0:
        break

    # 4개 벽 + 천장 면적
    wall_area = 2 * (width * height) + 2 * (length * height)
    ceiling_area = width * length
    paint_area = wall_area + ceiling_area

    # 문/창문 면적 빼기
    for _ in range(m):
        w, h = map(int, input().split())
        paint_area -= w * h

    # 아파트 개수 반영
    total_area = paint_area * n

    # 필요한 페인트 캔 수 (올림)
    cans = (total_area + area - 1) // area

    print(cans)