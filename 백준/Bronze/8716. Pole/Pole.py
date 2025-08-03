# GPT 4o
# 첫 번째 직사각형 입력
x1, y1, x2, y2 = map(int, input().split())
# 두 번째 직사각형 입력
x3, y3, x4, y4 = map(int, input().split())

# 겹치는 영역의 좌표 계산
left = max(x1, x3)
right = min(x2, x4)
top = min(y1, y3)
bottom = max(y2, y4)

# 겹치는 영역의 너비와 높이
width = right - left
height = top - bottom

# 교차하는 면적 계산 (음수일 경우 교차하지 않음 → 넓이 0)
if width > 0 and height > 0:
    print(width * height)
else:
    print(0)