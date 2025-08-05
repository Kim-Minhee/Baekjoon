# GPT 4o
n = int(input())
a = list(map(int, input().split()))

# 가장 왼쪽, 오른쪽 grusza(0) 위치
left_pear = a.index(0)
right_pear = n - 1 - a[::-1].index(0)

# 가장 왼쪽, 오른쪽 jabłoń(1) 위치
left_apple = a.index(1)
right_apple = n - 1 - a[::-1].index(1)

# 가능한 두 거리 중 큰 것
d1 = abs(right_apple - left_pear)
d2 = abs(right_pear - left_apple)

print(max(d1, d2))