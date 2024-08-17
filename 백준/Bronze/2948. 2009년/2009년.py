import calendar

# 입력
D, M = map(int, input().split())

# 풀이
day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
r = calendar.weekday(2009, M, D)

# 출력
print(day[r])